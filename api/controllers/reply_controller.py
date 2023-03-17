# Controller for handling replies
from utils.twitter import get_api
from models.tweet import Tweet
import tweepy
import time


def reply_to_mentions():
    api = get_api()
    mentions = api.mentions_timeline(since_id=Tweet.get_latest_tweet_id())

    # reversed for oldest first
    for mention in reversed(mentions):
        if mention.in_reply_to_status_id is not None:
            # if not a mention to b0bot then continue
            continue

        # user that mentions the b0bot
        user = mention.user.screen_name

        # the contents of the mentioned tweet
        text = mention.text

        # check if the mention has the #news hashtag
        if "#news" in text:
            # extract the keywords
            keywords = text.split("#news ")[1].split(" ")

            query = ' + '.join(keywords)

            # search for tweets with the keywords
            tweet = api.search(q=query, lang='en', result_type='recent', count=1)

            # reply with the latest tweet
            reply_text = f"Hi @{user}, here is the latest cybersecurity news on Twitter with the keywords: {', '.join(keywords)}\n"
            
            reply_text += f"\n{tweet.text}\n{tweet.user.name} (@{tweet.user.screen_name}): {tweet.created_at}\n"

            # reply to the mention
            api.update_status(reply_text, in_reply_to_status_id=mention.id)

        # to avoid rate limiting
        time.sleep(5)