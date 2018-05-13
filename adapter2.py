import database
from adapter import FacebookConsumer, TwitterConsumer


class FacebookAdapter(FacebookConsumer):

    def get_post(self):
        return super().get_latest_timeline_post()


class TwitterAdapter(TwitterConsumer):

    def gest_post(self):
        return super().get_latest_tweet()


def store_post(consumer):
    post = consumer.get_post()

    database.posts(post).save()


adapted_facebook_consumer = FacebookAdapter('some-token')

store_post(adapted_facebook_consumer)

adapted_twitter_consumer = TwitterAdapter('some-token')

store_post(adapted_twitter_consumer)
