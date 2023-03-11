# Model for storing tweet data
from datetime import datetime
from utils.mongo import get_db

class Tweet:
    def __init__(self, id, text, author, created_at=None):
        self.id = id
        self.text = text
        self.author = author
        self.created_at = created_at or datetime.utcnow()

    def save(self):
        db = get_db()
        db.tweets.insert_one({
            'id': self.id,
            'text': self.text,
            'author': self.author,
            'created_at': self.created_at
        })

    @classmethod
    def get_tweet_by_id(cls, tweet_id):
        db = get_db()
        tweet = db.tweets.find_one({'id': tweet_id})
        if tweet:
            return cls(
                id=tweet['id'],
                text=tweet['text'],
                author=tweet['author'],
                created_at=tweet['created_at']
            )
        return None
    
    @classmethod
    def get_latest_tweet_id(cls):
        db = get_db()
        tweet = db.tweets.find_one(sort=[('created_at', -1)])
        if tweet:
            return tweet['id']
        return None