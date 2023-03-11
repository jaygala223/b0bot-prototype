# Controller for handling replies
from utils.twitter import get_api
from models.tweet import Tweet
import time

def reply_to_mentions():
    api = get_api()
    mentions = api.mentions_timeline(since_id = Tweet.get_latest_tweet_id())

    #reversed for oldest first
    for mention in reversed(mentions):
        if mention.in_reply_to_status_id() is not None:
            # if not a mention to b0bot then continue
            continue

        # user that mentions the b0bot
        user = mention.user.screen_name

        # the contents of the mentioned tweet
        text = mention.text

        # a standard reply
        reply_text = f"Hi @{user}, thanks for mentioning me! I'm B0Bot, a Twitter bot that provides periodic cybersecurity and hacker news to the followers of Bug Zero Twitter account."

        # reply to the mention
        api.update_status(reply_text, in_reply_to_status_id=mention.id)

        # to avoid rate limiting
        time.sleep(5)
