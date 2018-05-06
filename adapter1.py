from adapter import FacebookConsumer, TwitterConsumer


class FacebookAdapter:

    def __init__(self, facebook_consumer):
        self.consumer = facebook_consumer

    def get_post(self):
        return self.consumer.get_lastest_timeline_post()


class TwitterAdapter:

    def __init__(self, twitter_consumer):
        self.consumer = twitter_consumer

    def get_post(self):
        return self.consumer.get_lastest_tweet()


def store_post(consumer):
    post = consumer.get_post()

    database.posts(post).save()


facebook_consumer = FacebookConsumer('some-token')
adapted_facebook_consumer = FacebookAdapter(facebook_consumer)

store_post(adapted_facebook_consumer)

twitter_consumer = TwitterConsumer('some-token')
adapted_twitter_consumer = TwitterAdapter(twitter_consumer)

store_post(adapted_twitter_consumer)
