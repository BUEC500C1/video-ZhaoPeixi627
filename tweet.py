# !/usr/bin/env python3

import tweepy #https://github.com/tweepy/tweepy
import json
import twitter_keys
import os

def get_tweet(User):    
    #Twitter API credentials
    consumer_key = twitter_keys.consumer_key
    consumer_secret = twitter_keys.consumer_secret
    access_key = twitter_keys.access_key
    access_secret = twitter_keys.access_secret

    handle = User

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #initialize a list to hold all the tweepy Tweets
    alltweets = [] 
    os.mkdir(User+'_'+'Photo')  

    #make initial request for most recent tweets (200 is the maximum allowed count)
    try:
        new_tweets = api.user_timeline(screen_name = handle, count=10, tweet_mode="extended")  #get most recent 10 tweets from the user
        if new_tweets == []:
            print("This user has no tweets yet")
        else:
            #save most recent tweets
            alltweets.extend(new_tweets) 
    except tweepy.TweepError as ex:
        if ex.reason == "Not authorized.":
            print("This is a private account, cannot access")
        else:
            print("Error: ",ex.reason) 
    res = []
    for i in range(len(alltweets)):
        res.append(alltweets[i].full_text)
    return res, User
    

##  test get_tweet('realDonaldTrump')  
##  test get_tweet('MikeBloomberg')





