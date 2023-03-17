# Controller for handling retweets
from utils.twitter import get_api
import tweepy
import time

def retweet_news():
    api = get_api()

    # search for tweets with the hashtag #cybersecuritynews
    query = '#cybersecuritynews'
    tweets = api.search(q=query, lang='en', result_type='recent', count=10)

    # loop through the tweets and retweet them
    for tweet in tweets:
        if not tweet.retweeted:
            try:
                api.retweet(tweet.id)
                print(f"Retweeted tweet with id {tweet.id}")
                time.sleep(5)
            except tweepy.TweepError as e:
                print(f"Error retweeting tweet with id {tweet.id}: {e}")

set_hours = 24

while True:
    retweet_news()
    time.sleep(set_hours * 60 * 60)