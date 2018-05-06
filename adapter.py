from requests_oauthlib import OAuth2

class FacebookTimelineConsumer:

	def __init__(self, api_token):
		self._api_token = api_token

	def get_lastest_timeline_post(self):
		return requests.get(
			'https://api.facebook.com/some-url', 
			auth=OAuth2('params..'))


class TwitterFeedConsumer:

	def __init__(self, api_token):
		self._api_token = api_token

	def get_lastest_tweet(self):
		return requests.get(
			'https://api.facebook.com/some-url', 
			auth=OAuth2('params..'))


def store_timeline_post(facebook_consumer):
	post = facebook_consumer.get_lastest_timeline_post()

	database.posts(post).save()


def store_tweet(twitter_consumer):
	tweet = twitter_consumer.get_lastest_tweet()

	database.posts(tweet).save()
