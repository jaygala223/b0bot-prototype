#Functions that will support the interaction with MongoDB database
from pymongo import MongoClient
import os

# b0bot_db is name of the database in mongoDB

def get_db():
    client = MongoClient(os.environ.get('MONGO_URI'))
    return client[os.environ.get('b0bot_db')]