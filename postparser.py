#!/bin/python
import feedparser
import imp
from HTMLParser import HTMLParser
import plugins
from urllib2 import URLError
import yaml


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


def parse(feed):
    d = feedparser.parse(feed)
    if d.bozo:
        raise d.bozo_exception

    try:
        mastodon_post = d.entries[0]
    except IndexError:
        return

    post = {}

    post['link'] = mastodon_post.link
    post['date_time'] = mastodon_post.published
    post['summary'] = strip_tags(mastodon_post.summary)
    try:
        post['tags'] = mastodon_post.tags
    except AttributeError:
        exit()

    new_post = False

    try:
        with open('last_modified', 'r') as f:
            last_modified = f.readline()
            if last_modified < post['date_time']:
                new_post = True
        with open('last_modified', 'w') as f:
            f.write(post['date_time'])
    except IOError:
        new_post = True
        with open('last_modified', 'w') as f:
            f.write(post['date_time'])

    if new_post:
        for name in plugins.__all__:
            # Load plugin and post
            package_info = imp.find_module(name, ['plugins'])
            social_outlet = imp.load_module(name, *package_info)
            social_outlet.post(post)


config_location = 'config.yml'
config = {}
try:
    with open(config_location, 'r') as stream:
        try:
            config = yaml.load(stream)['config']
        except yaml.YAMLError as e:
            print(e)
except IOError:
    print("Please create config: {}".format(config_location))

feed = config['feed']
try:
    parse(feed)
except URLError:
    print("Mastodonw instance @ {} isn't accessible".format(feed))
