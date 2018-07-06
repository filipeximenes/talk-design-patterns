from time import sleep


class FacebookConsumer:

    def __init__(self, api_token):
        self._api_token = api_token

    def make_request(self, url):
        ...

    def get_latest_timeline_post(self):
        print('Fetching from Facebook')
        sleep(1)
        return self.make_request('some-url')

    ...


class TwitterConsumer:

    def __init__(self, api_token):
        self._api_token = api_token

    def make_request(self, url):
        ...

    def get_latest_tweet(self):
        print('Fetching from Twitter')
        sleep(1)
        return self.make_request('some-url')

    ...
