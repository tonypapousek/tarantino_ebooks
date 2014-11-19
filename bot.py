#!/usr/bin/env python

from twython import Twython

API_KEY = ''
API_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

twitter = Twython(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


search_results = twitter.search(q="English motherfucker do you speak it",count=10)


for tweet in search_results['statuses']:
    tweet_username = tweet['user']['screen_name'].encode('utf-8')
    bot_reply = "@%s What?" % (tweet_username)
    try:
        twitter.update_status(status=bot_reply, in_reply_to_status_id=tweet['id'])
        print HttpResponse("1", content_type='text/plain')
    except:
        print "Error. Twitter won't let us reply to @%s's tweet." % (tweet_username)
