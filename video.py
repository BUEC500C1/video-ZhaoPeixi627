# !/usr/bin/env python3


import os
import cv2
import image
from tweet import get_tweet
from image import textToImg

def imgToVideo(user):
    # [user] = get_tweet(user)
    [filepath,users] = textToImg(user)
    temp = os.getcwd() # get current directory 
    mid = str(temp)
    new = mid.replace("\\",'/')
    path = new + filepath 
    # print(path)
    file_dir = (f'{path}')
    # file_dir = (f'{filepath}')
    list=[]
    for  root,dirs,files in os.walk(file_dir):
        for file in files:
           list.append(file)  
    # print(list)
    list.sort()
    video=cv2.VideoWriter(f'./{users}.avi',cv2.VideoWriter_fourcc(*'MJPG'),0.333,(1960,1080)) 
    for i in range(0,len(list)):
        img=cv2.imread(f'{path}'+list[i])
        # print(f'{path}'+list[i])
        img=cv2.resize(img,(1960,1080)) # resize the image to(1960,1080)
        video.write(img)



##  test use imgToVideo('realDonaldTrump')  
## test use imgToVideo('MikeBloomberg')
