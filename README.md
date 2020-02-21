# video-ZhaoPeixi627
video-ZhaoPeixi627 created by GitHub Classroom
## The technology I use to do this homework.
1. Programming Language: Python 3.7

![](https://github.com/BUEC500C1/video-ZhaoPeixi627/blob/master/ReadMePhoto/pylogo.png)

2. Twitter API(Tweepy): Use this API to get twitter comments from the users.

![](https://github.com/BUEC500C1/video-ZhaoPeixi627/blob/master/ReadMePhoto/twitter.jpg)

3. PIL Libaray(Pillow): To create a image and write text on the image.

![](https://github.com/BUEC500C1/video-ZhaoPeixi627/blob/master/ReadMePhoto/python-pillow-logo.png)

4. OPEN CV(cv2): To create a video based on different photos.

![](https://github.com/BUEC500C1/video-ZhaoPeixi627/blob/master/ReadMePhoto/download.png)

5. Queue Threading: To create a queue to allocate each thread.

![](https://github.com/BUEC500C1/video-ZhaoPeixi627/blob/master/ReadMePhoto/Queue.png)


## Set Up
### Twitter API 
To run the twitter API, users need to import their own API keys.
### cv2
Users need to install the opencv enviornment before they use cv2. Command is : pip install pip install openCV-python.
### Font
Users need to include the STIXGeneral.ttf in the file to run the program.
### Images
I set the images size as (1960,1024) and color(30,144,255). And I set the text to write at the position of (10,200) in the image.
### Video
I set the video fps as 0.333 and resize the image to (1960,1024).


## Step of the homework
### 1.Develop a queue system that can exercise your requirements with stub functions.

### 2.Develop the twitter functionality with an API

### 3.Integrate them

## To Run this Program
After setting up all prerequiste enviornment, just run the sys.py. Then you will get the User + _ + photo file which store the photos which have the twitters' comments on it and a video of that specific user.

## Result
### The photos of the user's twitter comments.

![](https://github.com/BUEC500C1/video-ZhaoPeixi627/blob/master/ReadMePhoto/coldplayphoto.png)

### The video

![](https://github.com/BUEC500C1/video-ZhaoPeixi627/blob/master/ReadMePhoto/video.png)

### The Threading

![](https://github.com/BUEC500C1/video-ZhaoPeixi627/blob/master/ReadMePhoto/Threading.png)

## Material I learnt for this exercise
1. Python Queues
2. Python processes and subprocesses
3. Python Threads
4. Python Threads Versus Processes
5. Python asyncio
6. FFMPEG

## Homework Question
1. How many API calls you can handle simultaneously and why?
I call one API since I just use one API which is Tweepy.
2. or example, run different API calls at the same time?
Yes, I can calls several APIs at the same time.
3. Split the processing of an API into multiple threads?
I split the process to 5 threads.


