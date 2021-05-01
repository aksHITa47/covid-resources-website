import os
from dotenv import load_dotenv
import tweepy
import time
import pandas as pd

load_dotenv()
consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit = True)


def get_tweets(city, resource):
    query = "verified {} {} -not verified -un verified -urgent -unverified -needed -required -need -needs since:2021-4-26".format(city, resource)
    count = 15

    try:
        tweets = tweepy.Cursor(api.search, q = query).items(count)

        tweets_list = [[tweet.created_at, tweet.id, tweet.text] for tweet in tweets]
        tweets_df = pd.DataFrame(tweets_list)

    except BaseException as e:
        print("failed", str(e))
        time.sleep(3)
    
    return tweets_df


get_tweets('Hyderabad', 'oxygen')