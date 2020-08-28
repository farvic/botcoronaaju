import logging
import os
import tweepy

logger = logging.getLogger()

def create_api():
    print('calling function')
    consumer_key = os.getenv("TWITTER_API_KEY")
    consumer_secret = os.getenv("TWITTER_API_KEY_SECRET")
    access_token = os.getenv("TWITTER_ACCESS_TOKEN")
    access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
        print('came here')
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api

# print('calling function')
# consumer_key = os.getenv("TWITTER_API_KEY")
# consumer_secret = os.getenv("TWITTER_API_KEY_SECRET")
# access_token = os.getenv("TWITTER_ACCESS_TOKEN")
# access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# # Authenticate to Twitter
# auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
# auth.set_access_token(access_token,access_token_secret)

# api = tweepy.API(auth)

# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except:
#     print("Error during authentication")