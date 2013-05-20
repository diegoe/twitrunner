#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# twitrunner - an extra simple twitter miner
#
# Author: Diego Escalante Urrelo <diegoe@gnome.org>
# URL: https://github.com/diegoe/twitrunner
#
# A very, very, simple data miner for twitter.

import codecs
import tweepy

# keys.txt is a file made up of 4 lines:
# consumer_key
# consumer_secret
# consumer_token
# consumer_token_secret
#
# You need to get this keys from your twitter developer account:
# https://dev.twitter.com/apps

keys = open("keys.txt").readlines()

consumer_key = keys[0].strip()
consumer_secret = keys[1].strip()

access_token = keys[2].strip()
access_token_secret = keys[3].strip()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
print "Authenticated as: %s (%s)" % (api.me().name, api.me().screen_name)

with codecs.open("users.txt", "r", "utf-8") as f:
    users = f.readlines()

for teacher in users:
    name, university, topics, userid = teacher.strip().split("\t")

    try:
        p = api.get_user(userid)
        print "%s\t%s\t%s\t%s\thttps://twitter.com/%s" % \
            (name, university, topics, p.followers_count, userid)
    except:
        print "@id is not a valid twitter ID"
