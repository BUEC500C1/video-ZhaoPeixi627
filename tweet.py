# !/usr/bin/env python3

import tweepy #https://github.com/tweepy/tweepy
import json
import keys
import os

def get_tweet(User):    
    #Twitter API credentials
    if keys.consumer_key != "":  #only excecute when there is a key

        consumer_key = keys.consumer_key
        consumer_secret = keys.consumer_secret
        access_key = keys.access_key
        access_secret = keys.access_secret


        handle = User

        #authorize twitter, initialize tweepy
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth)

        #initialize a list to hold all the tweepy Tweets
        alltweets = [] 

        # os.mkdir(User+'_'+'Photo')   ### !!!!!!!!!!!!!!! Need to uncomment this before locally testing !!!!!!!!!!!!!!

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
        
        dic = {}
        dic[User] = res
        jsonData = json.dumps(dic)
        fileObject = open(User + '.json', 'w')
        fileObject.write(jsonData)
        fileObject.close()
        return res, User

    
    else:
        name = User + '.json'
        new_dict = open(name,encoding='utf-8')
        dictionary = json.load(new_dict)
        for i in dictionary.values():
            res = i
        for j in dictionary.keys():
            User = j
        return res, User
    

##  test get_tweet('realDonaldTrump')  
##  test get_tweet('MikeBloomberg')





