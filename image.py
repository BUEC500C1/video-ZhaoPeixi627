# !/usr/bin/env python3

import os
from PIL import Image, ImageDraw, ImageFont   # for text on image 
from tweet import get_tweet


def textToImg(user):
    # img = Image.new('RGB',(1280,1024),color = (255,106,106))
    # new = os.mkdir(user+'Photo')
    [text,users] = get_tweet(user)
    for i in range(len(text)):
        ft = ImageFont.truetype('./STIXGeneral.ttf',40) 

        img = Image.new('RGB',(1960,1024),color = (30,144,255))  #to create a new image

        d = ImageDraw.Draw(img)
        # url_reg = r'[a-z]*[:.]+\S+' 
        # text[i] = re.sub(url_reg, '', text[i])
        # to adjust the tweets to fit into the image
        text[i] = text[i].encode('ascii','ignore').decode('ascii') 
        text[i] = text[i].replace(". ", ".\n")
        text[i] = text[i].replace(", ", ",\n")
        text[i] = text[i].replace("! ", "!\n")
        text[i] = text[i].replace("; ", ";\n")
        text[i] = text[i].replace("? ", "?\n")
        text[i] = text[i].replace("  ", " \n")

        d.text((10,200), text[i],font = ft,fill=(0,0,0)) # to write tweet in image

        filename = './'+ users+'_'+'Photo/' +  users + str(i) +".jpg" 
        img.save(filename) # save images to the file 
        path = './'+ users+'_'+'Photo/'
        
    return path,users

##  test use textToImg('realDonaldTrump')  
##  test use textToImg('MikeBloomberg')

