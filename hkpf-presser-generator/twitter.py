import tweepy
from datetime import date
import os
import trigrams


def post_tweet():
    api_key = os.environ["HKPFG_TWITTER_API_KEY"]
    api_secret_key = os.environ["HKPFG_TWITTER_API_SECRET_KEY"]
    access_token = os.environ["HKPFG_TWITTER_ACCESS_TOKEN"]
    access_token_secret = os.environ["HKPFG_TWITTER_ACCESS_TOKEN_SECRET"]

    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    try:
        message = trigrams.generate_random_sentence()
        api.update_status(message)
        return {
            'statusCode': 200
        }
    except tweepy.TweepError as e:
        return {
            'statusCode': e.message[0]['code']
        }


# divide the message up into 280-character tweets
def split_into_tweets(message):
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


test_message = "Are own design entire former get should. Advantages boisterous day excellence boy. Out between our two waiting wishing. Pursuit he he garrets greater towards amiable so placing. Nothing off how norland delight. Abode shy shade she hours forth its use. Up whole of fancy ye quiet do. Justice fortune no to is if winding morning forming. Improve him believe opinion offered met and end cheered forbade. Friendly as stronger speedily by recurred. Son interest wandered sir addition end say. Manners beloved affixed picture men ask. Explain few led parties attacks picture company. On sure fine kept walk am in it. Resolved to in believed desirous unpacked weddings together. Nor off for enjoyed cousins herself. Little our played lively she adieus far sussex. Do theirs others merely at temper it nearer."
print(split_into_tweets(test_message))