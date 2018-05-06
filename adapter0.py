from adapter import FacebookConsumer, TwitterConsumer


def store_timeline_post(facebook_consumer):
    post = facebook_consumer.get_lastest_timeline_post()

    database.posts(post).save()


def store_tweet(twitter_consumer):
    tweet = twitter_consumer.get_lastest_tweet()

    database.posts(tweet).save()
