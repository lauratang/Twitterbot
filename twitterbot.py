#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tutorial by @robincamille - for @mechnicalpoe
# Tutorial: http://emerging.commons.gc.cuny.edu/2013/10/making-twitter-bot-python-tutorial/

# Must be running all the time, e.g. on a Raspberry Pi, but would be better 
# if configured to run as a cron task.

import tweepy, time

# Variables contain user credentials
CONSUMER_KEY = 'xxx' # To get this stuff, sign in at https://dev.twitter.com/ and Create a New Application
CONSUMER_SECRET = 'xxx' # Make sure access level is Read And Write in the Settings tab
ACCESS_KEY = 'xxx' # Create a new Access Token
ACCESS_SECRET = 'xxx'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Helper method to direct message a follower
def process_friend(friend):
    print (friend.screen_name)
    # message = 'Outage detected in your area, ' + time until restoration
    # or message = 'Outage resolved, thank you for your patience'
    # api.send_direct_message(user = friend.screen_name, text = "hello")

# INFINITE LOOP HERE listening for new outage update in database to enter loop
# When a new outage is added / resolved in database ->

# 1. We update our own status
api.update_status(status = 'Success')

# 2. Follow back all of our friends
# for follower in tweepy.Cursor(api.followers).items():
    # follower.follow()

# 3. Iterate through all of the our friends
for friend in tweepy.Cursor(api.friends).items():
    # query our database for the screenname's and location
    # if location matches that of an outage
        process_friend(friend)
        time.sleep(0) # sleep for 0 seconds, increase to avoid rate ban(?)
        
