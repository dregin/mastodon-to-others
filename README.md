# mastodon-to-others

## Description
Script to post the last post you made on Mastodon to other social media.
Plugins included are for twitter and facebook.

## Installation
Clone the repo and run `postparser.py` from cron
Update configs in config directory to reflect your settings

## Cron
```
* * * * * cd /opt/mastodon-to-others/ && /usr/bin/python /opt/mastodon-to-others/postparser.py
```
