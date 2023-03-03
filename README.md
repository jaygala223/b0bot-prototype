# b0bot-prototype
prototype for b0bot project at GSoC 2023 SCoRe labs

## Project Requirements
1. B0Bot is a Twitter bot that provides periodic news to the followers of Bug Zero Twitter account
2. B0Bot will provide latest news to a user who mentions the Bug Zero Twitter account and ask for certain keywords
3. B0Bot will live inside a Flask API
4. B0Bot will periodically retweet certain Twitter accounts
5. B0Bot will reply with information if a user mentions the bot
6. B0Bot will periodically run as a serverless function


## Roadmap
1. Set up a Twitter developer account and create a new app to access the Twitter API (applied... waiting for account activation)
2. Install and configure the Tweepy library to interact with the Twitter API using Python
3. Set up a MongoDB database using PyMongo to store the data collected by B0Bot
4. Set up a Flask API that handles incoming requests from Twitter and users
5. Implement B0Bot's periodic news feature by configuring the Tweepy library to periodically collect and store data from the Twitter API
6. Implement B0Bot's keyword search feature by setting up a webhook to receive and process user requests from Twitter
7. Implement B0Bot's retweet feature by configuring the Tweepy library to retweet tweets from certain accounts
8. Implement B0Bot's reply feature by processing user mentions and sending appropriate responses
9. Deploy B0Bot as a serverless function using Vercel