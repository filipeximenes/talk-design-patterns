from adapter import FacebookTimelineConsumer, TwitterFeedConsumer


class FacebookAdapter(FacebookTimelineConsumer):

	def get_post(self):
		return super().get_latest_timeline_post()


class TwitterAdapter(TwitterFeedConsumer):

	def gest_post(self):
		return super().get_latest_tweet()


adapted_facebook_consumer = FacebookAdapter('some-token')

store_post(adapted_facebook_consumer)

adapted_twitter_consumer = TwitterAdapter('some-token')

store_post(adapted_twitter_consumer)
