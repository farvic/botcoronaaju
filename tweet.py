import tweepy
import os

# Authenticate to Twitter
# auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
# auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler(os.getenv("TWITTER_API_KEY"), TWITTER_API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# # Create API object
# api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# # Create a tweet
# api.update_status("Hello Tweepy")