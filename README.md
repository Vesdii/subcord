# Subcord

This Python script fetches information about YouTube videos of a list of channels and posts them to a Discord webhook if they have not been posted already.

The already posted videos are tracked via the `ignore_videos` dump file, listing the IDs.

Example of `channels.conf`:

```
https://discord.com/api/webhooks/XXXXX/XXXXX

UCvF7Ll_WOgQWOw0KZJsVNXQ
UCfe_znKY1ukrqlGActlFmaQ
```

## Implementation

I recommend running this with a cronjob scheduler every hour or so. For example, your crontab could contain:

```
5 * * * * python3 ~/subcord/subcord.py
```
