from adapter import FacebookConsumer, TwitterConsumer


def store_timeline_post(facebook_consumer):
    post = facebook_consumer.get_lastest_timeline_post()

    database.posts(post).save()


def store_tweet(twitter_consumer):
    tweet = twitter_consumer.get_lastest_tweet()

    database.posts(tweet).save()


facebook_consumer = FacebookConsumer('some-token')
store_timeline_post(facebook_consumer)

twitter_consumer = TwitterConsumer('some-token')
store_tweet(twitter_consumer)
