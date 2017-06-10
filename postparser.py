#!/bin/python
import feedparser
from HTMLParser import HTMLParser


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
    for post in d.entries:
        title = post.title
        summary = strip_tags(post.summary)
        link = post.link
        date_time = post.published

        print('{}'.format(title))
        print('\t{}'.format(summary))
        print('\t{}'.format(link))
        print('\t{}'.format(date_time))


feed = 'https://mastodon.redbrick.dcu.ie/users/dregin.atom'
parse(feed)
