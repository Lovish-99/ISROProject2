from __future__ import absolute_import, unicode_literals
#importing libraries and modules
from celery import shared_task
import time
import hashlib
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import os
from .runtime1 import create_csv
from .runtime2 import create_csv4
from .runtime3 import create_csv5
from .runtime4 import create_csv2
from background_task import background
from django.contrib.auth.models import User

@background(schedule=60)
def notify_user(user_id):
    # lookup user by id and send them a message
    user = User.objects.get(pk=user_id)
    user.email_user('Here is a notification', 'You have been notified')

@shared_task
def add(x, y):
    time.sleep(10)
    return x + y

@shared_task
def send_email(email_id, message):
    time.sleep(10)
    print(add(5,9))
    print(f"Email is sent to {email_id}. Message sent was - {message}")

@shared_task
def notifier():
    # setting the URL we want to monitor
    url = Request('http://125.19.52.219/wqi/', headers={'User-Agent': 'Mozilla/5.0'})
    print("running")
    #monitering the website
    try:
        #open file in read mode and get the old hashcode of the site
        file = open("map/hashcode.txt","r")
        currentHash = file.readline()
        file.close()
        # perform the get request
        response = urlopen(url).read()
        # create a new hash
        newHash = hashlib.sha224(response).hexdigest()
        # check if new hash is same as the previous hash
        if newHash == currentHash:
            print("Data not updated")
            time.sleep(5)
            print("Process is Done!")
        # if something changed in the hashes
        else:
            # notify
            print("Data updated")
            #calling the function to create updaed csv files and plots
            create_csv()
            time.sleep(10)
            #create a file, write it and close it
            file = open("map/hashcode.txt","w+")
            file.write(newHash)
            file.close()

            print("Process is Done!")
    #handling exceptions
    except Exception as e:
        print("error",e)

@shared_task
def notifier2():
    # setting the URL we want to monitor
    url = Request('http://125.19.52.219/wqi/dinkingB.php', headers={'User-Agent': 'Mozilla/5.0'})
    print("running")
    #monitering the website
    try:
        #open file in read mode and get the old hashcode of the site
        file = open("map/hashcode_2.txt","r")
        currentHash = file.readline()
        file.close()
        # perform the get request
        response = urlopen(url).read()
        # create a new hash
        newHash = hashlib.sha224(response).hexdigest()
        # check if new hash is same as the previous hash
        if newHash == currentHash:
            print("Data not updated")
            time.sleep(5)
            print("Process is Done!")
        # if something changed in the hashes
        else:
            # notify
            print("Data updated")
            #calling the function to create updaed csv files and plots
            create_csv4()
            time.sleep(10)

            #create a file, write it and close it
            file = open("map/hashcode_2.txt","w+")
            file.write(newHash)
            file.close()

            print("Process is Done!")
    #handling exceptions
    except Exception as e:
        print("error",e)

@shared_task
def notifier3():
    # setting the URL we want to monitor
    url = Request('http://125.19.52.219/wqi/bathing.php', headers={'User-Agent': 'Mozilla/5.0'})
    print("running")
    #monitering the website
    try:
        #open file in read mode and get the old hashcode of the site
        file = open("map/hashcode_3.txt","r")
        currentHash = file.readline()
        file.close()
        # perform the get request
        response = urlopen(url).read()
        # create a new hash
        newHash = hashlib.sha224(response).hexdigest()
        # check if new hash is same as the previous hash
        if newHash == currentHash:
            print("Data not updated")
            time.sleep(5)
            print("Procss is Done!")
        # if something changed in the hashes
        else:
            # notify
            print("Data updated")
            #calling the function to create updaed csv files and plots
            create_csv5()
            time.sleep(10)

            #create a file, write it and close it
            file = open("map/hashcode_3.txt","w+")
            file.write(newHash)
            file.close()

            print("Process is Done!")
    #handling exceptions
    except Exception as e:
        print("error",e)

@shared_task
def notifier4():
    # setting the URL we want to monitor
    url = Request('http://125.19.52.218/realtime/', headers={'User-Agent': 'Mozilla/5.0'})
    print("running")
    #monitering the website
    try:
        #open file in read mode and get the old hashcode of the site
        file = open("map/hash2code.txt","r")
        currentHash = file.readline()
        file.close()
        # perform the get request
        response = urlopen(url).read()
        # create a new hash
        newHash = hashlib.sha224(response).hexdigest()
        # check if new hash is same as the previous hash
        if newHash == currentHash:
            print("Data not updated")
            time.sleep(5)
            print("Process is Done!")
        # if something changed in the hashes
        else:
            # notify
            print("Data updated")
            #calling the function to create updaed csv files and plots
            create_csv2()
            time.sleep(10)

            #create a file, write it and close it
            file = open("map/hash2code.txt","w+")
            file.write(newHash)
            file.close()
                
            print("Process is Done!")
    #handling exceptions
    except Exception as e:
        print("error",e)