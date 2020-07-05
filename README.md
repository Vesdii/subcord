# Subcord

This Python script fetches information about YouTube videos of a list of channels and posts them to a Discord webhook if they have not been posted already.

The already posted videos are tracked via the `ignore_videos` dump file, listing the IDs.

`channels.conf` template (w/ line numbers):

```
 1  <Discord webhook URL>
 2  <(Optional) Discord role ID to mention>
 3  
 4  <YouTube channel ID>
 5  <YouTube channel ID> <Name of channel>
...
```

Text after a space serves as a comment for each line when listing channel IDs.

Mentioning can be disabled by leaving the line empty.

## Implementation

I recommend running this with a cronjob scheduler every hour or so. For example, your crontab could contain:

```
5 * * * * python3 ~/subcord/subcord.py
```
