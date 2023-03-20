# Controller for handling news requests
import tweepy
from utils.twitter import get_api
from utils.mongo import get_db
import pandas as pd

def add_news_to_db():
    api = get_api()

    keywords = 'cybersecurity + news'

    limit = 500

    #get 500 tweets from across twitter which contain the keywords
    tweets = tweepy.Cursor(api.search_tweets, q=keywords, count=200, tweet_mode = 'extended').items(limit)

    for tweet in tweets:
        pass


