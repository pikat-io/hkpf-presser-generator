import twitter
import trigrams


def awslambda_handler(event, context):
    message = trigrams.generate_random_sentence()
    return twitter.tweet(message)

