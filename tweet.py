import tweepy
import logging
from config import create_api
import time

from coronabot import data_web_scraping

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def follow_followers(api):
    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(f"Following {follower.name}")
            follower.follow()

def main():
    api = create_api()
    casos, obitos, isolamento = data_web_scraping()
    api.update_status(
                status='''
                Posting a tweet through the Twitter API.
                
                Testing...''')
    # while True:
    #     follow_followers(api)
    #     logger.info("Waiting...")
    #     time.sleep(60)

if __name__ == "__main__":
    main()