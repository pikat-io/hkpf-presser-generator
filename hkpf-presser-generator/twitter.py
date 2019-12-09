import tweepy
import os

# divide the message up into 280-character tweets
def __split_into_tweets(message):
    if len(message) <= 280:
        return [message]
    else:
        tweets = []
        words = message.split(' ')
        current_tweet_length = 0
        current_tweet = ""
        word_count = len(words)
        word_index = 0

        # clearly i know nothing about iterators in python
        for word in words:
            word_index += 1
            if current_tweet_length + len(word) <= 280:
                current_tweet_length += len(word)
                current_tweet += word

                if word_index is not word_count:
                    current_tweet_length += 1
                    current_tweet += " "
            else:
                tweets.append(current_tweet)
                current_tweet = ""
                current_tweet_length = 0

        if current_tweet != "":
            tweets.append(current_tweet)

        return tweets


def __post_tweets(tweets):
    api_key = os.environ["HKPFG_TWITTER_API_KEY"]
    api_secret_key = os.environ["HKPFG_TWITTER_API_SECRET_KEY"]
    access_token = os.environ["HKPFG_TWITTER_ACCESS_TOKEN"]
    access_token_secret = os.environ["HKPFG_TWITTER_ACCESS_TOKEN_SECRET"]

    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    try:
        previous_response = None
        for tweet in tweets:
            if previous_response is None:
                previous_response = api.update_status(tweet)
            else:
                previous_response = api.update_status(tweet, previous_response.id)

        return {
            'status_code': 200,
            'reason': None
        }
    except tweepy.TweepError as e:
        return {
            'status_code': e.response.status_code,
            'reason': e.reason
        }


def tweet(message):
    tweets = __split_into_tweets(message)
    return __post_tweets(tweets)