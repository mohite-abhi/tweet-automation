import tweepy
import json
from cred import *
import time
import os
from imgurUpload import upload_image

def check_ping():
    hostname = "google.com"
    response = os.system("ping -n 1 " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = 1
    else:
        pingstatus = 0
    
    return pingstatus


def upload_tweet(msg):
    client = tweepy.Client(consumer_key=apikey,
                        consumer_secret=apikeysecret,
                        access_token=accesstoken,
                        access_token_secret=accesstokensecret)

    try:
        response = client.create_tweet(text=msg)
    except:
        return 0
    if not response.errors:
        return 1
    return 0


def load_tweet():
    try:
        with open('content.json', 'r', encoding="utf8") as filestream:
            content_arr = json.load(filestream)[::-1]
            if content_arr:
                content = content_arr.pop()
                msg = content["msg"]
                media = content["media"]
                if media:
                    link = upload_image(media)
                else:
                    link = ""
                msg = msg + " " + link
                with open('content.json', 'w') as filestream:
                    json.dump(content_arr[::-1], filestream, indent=4)
                return msg[:280]
            else:
                return ''          
    except Exception as e:
        print(e)
        return ''


def start_tweet_routine(interval_in_sec = 30, max_number = 120):
    for i in range(120):
        next_tweet = load_tweet()
        print("Tweet: ",next_tweet[:5],"... Uploaded Successfully!")
        if next_tweet == '':
            continue
        upload_status = upload_tweet(next_tweet)
        if upload_status == 0:
            return
        time.sleep(interval_in_sec)


if __name__ == "__main__":
    internet_working = check_ping()
    if not internet_working:
        print("Internet not working")
    else:
        start_tweet_routine(interval_in_sec=10)