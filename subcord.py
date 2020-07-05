import requests
import xml.etree.ElementTree as ET

def get_feed(channel):
    res = requests.get(f'https://www.youtube.com/feeds/videos.xml?channel_id={channel}')
    if res.status_code != 200:
        return None
    root = ET.fromstring(res.text)

    # Some stupid prefix that it puts in front of every tag name
    pfx = '{http://www.w3.org/2005/Atom}'

    feed = { 'author': root.find(pfx+'title').text, 'videos': [] }

    for entry in root.iter(pfx+'entry'):
        vid = {}
        vid['title'] = entry.find(pfx+'title').text
        vid['link'] = entry.find(pfx+'link').get('href')
        vid['id'] = entry.find(pfx+'id').text.split(':')[2]
        feed['videos'].append(vid)
        #all_videos.add(vid['id'])

    return feed

# Parse config file
webhook = None
channels = None
with open('channels.conf') as f:
    conf = f.read().split('\n')
    webhook = conf[0]
    channels = conf[2:-1]
    # Ignore comment after ID
    channels = [x.split(' ')[0] for x in channels]

# Create ignore file if it doesn't exist
# NOTE: This method creates a file with a single newline character
open('ignore_videos', 'a').close()
# Parse ignore file
ignore_videos = None
with open('ignore_videos') as f:
    ignore_videos = set(f.read().split('\n'))

#all_videos = set()
posted = False

for channel in channels:
    feed = get_feed(channel)
    if not feed:
        print('FAILURE: '+channel)
        continue

    post_data = {}
    post_data['username'] = feed['author']

    # Post unposted videos
    for video in feed['videos']:
        if video['id'] in ignore_videos:
            continue
        post_data['content'] = video['title'] + '\n' + video['link']
        requests.post(webhook, data = post_data)
        print(video['id'])
        ignore_videos.add(video['id'])
        posted = True

# TODO: remove ignored videos no longer in list of all videos

if posted:
    with open('ignore_videos', 'w') as f:
        f.write('\n'.join(ignore_videos))
