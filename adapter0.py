import database
from adapter import FacebookConsumer, TwitterConsumer


def store_timeline_post(facebook_consumer):
    post = facebook_consumer.get_latest_timeline_post()

    database.add_post(post)


def store_tweet(twitter_consumer):
    tweet = twitter_consumer.get_latest_tweet()

    database.add_post(tweet)


facebook_consumer = FacebookConsumer('some-token')
store_timeline_post(facebook_consumer)

twitter_consumer = TwitterConsumer('some-token')
store_tweet(twitter_consumer)
