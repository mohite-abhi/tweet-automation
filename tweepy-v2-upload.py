import tweepy
import json
from cred import *
import time

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
                msg = content_arr.pop()["msg"]
                with open('content.json', 'w') as filestream:
                    json.dump(content_arr[::-1], filestream, indent=4)
                return msg
            else:
                return ''          
    except Exception as e:
        print(e)
        return ''


def start_tweet_routine(interval_in_sec = 30, max_number = 120):
    for i in range(120):
        next_tweet = load_tweet()
        print("Tweet",next_tweet[:5],"... Uploaded Successfully!")
        if next_tweet == '':
            continue
        upload_status = upload_tweet(next_tweet)
        if upload_status == 0:
            return
        time.sleep(interval_in_sec)


start_tweet_routine(interval_in_sec=10)