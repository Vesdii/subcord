# Subcord

This Python script fetches information about YouTube videos of a list of channels and posts them to a Discord webhook if they have not been posted already.

The already posted videos are tracked via the `ignore_videos` dump file, listing the IDs.

Now includes the ability to mention roles/members using mention id.

Example of `channels.conf`:

```
https://discord.com/api/webhooks/XXXXX/XXXXX
<mention_id>

UCvF7Ll_WOgQWOw0KZJsVNXQ Elisha Long
UCfe_znKY1ukrqlGActlFmaQ Healthy Software Developer
```

Text preceded by a space serves as a comment for each line when listing channel IDs.

Mentioning can be disabled by leaving a space.
**Channel ids must start on the 4th line**

## Implementation

I recommend running this with a cronjob scheduler every hour or so. For example, your crontab could contain:

```
5 * * * * python3 ~/subcord/subcord.py
```