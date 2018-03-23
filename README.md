# mastodon-to-others

## Description
Script to share Mastodon posts with a specific hash tag (default is #share) to other social media.
Plugins included are for twitter and ifttt.

## Installation
Clone the repo and run `postparser.py` from cron
Update configs in config directory to reflect your settings

## Cron
```
* * * * * cd /opt/mastodon-to-others/ && /usr/bin/python /opt/mastodon-to-others/postparser.py
```
