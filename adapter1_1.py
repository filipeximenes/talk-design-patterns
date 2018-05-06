from adapter import FacebookConsumer, TwitterConsumer


class PostAdapter:

    def __init__(self, consumer, method_name):
        self.consumer = consumer
        self.method_name = method_name

    def get_post(self):
        method = getattr(self.consumer, self.method_name)
        return method()


def store_post(consumer):
    post = consumer.get_post()

    database.posts(post).save()


facebook_consumer = FacebookConsumer('some-token')
adapted_facebook_consumer = PostAdapter(facebook_consumer, 'get_lastest_timeline_post')

store_post(adapted_facebook_consumer)

twitter_consumer = TwitterConsumer('some-token')
adapted_twitter_consumer = PostAdapter(twitter_consumer, 'get_lastest_tweet')

store_post(adapted_twitter_consumer)
