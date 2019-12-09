import tweepy
from datetime import date
import os


def post_tweet():
    api_key = os.environ["HKPFG_TWITTER_API_KEY"]
    api_secret_key = os.environ["HKPFG_TWITTER_API_SECRET_KEY"]
    access_token = os.environ["HKPFG_TWITTER_ACCESS_TOKEN"]
    access_token_secret = os.environ["HKPFG_TWITTER_ACCESS_TOKEN_SECRET"]

    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    try:
        now = date.today().strftime("%B %d, %Y")
        message = "As of " + now + ", the Hong Kong Police Force is still insane."
        api.update_status(message)
        return {
            'statusCode': 200
        }
    except tweepy.TweepError as e:
        return {
            'statusCode': e.message[0]['code']
        }


post_tweet()