# !/usr/bin/env python3


import time
import queue
import threading
from tweet import get_tweet
from image import textToImg
from video import imgToVideo


def worker(i):
    while True:
        item = q.get()
        if item is None:
            print('no item to work now')
            break
        time.sleep(0.5)
        imgToVideo(item)
        print("Current work is finished:" , item)
        q.task_done()


if __name__ == '__main__':
    num_of_threads = 5 

    user_name = ['realDonaldTrump','MikeBloomberg','kanyewest','Eminem','Cristiano','kobebryant','DCBatman','DCSuperman','QueenWillRock','coldplay'] 


    # Build FIFO Queue
    q = queue.Queue()
    # build Threads
    threads = []

    # creat and put threads
    for i in range(1, num_of_threads+1):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    # put item into queue
    for item in user_name:
        time.sleep(0.5)     # 0.5 second per item
        q.put(item)

  
    q.join()
    print("-----work finished-----")

    for i in range(num_of_threads):
        q.put(None)
    for t in threads:
        t.join()
    print(threads)