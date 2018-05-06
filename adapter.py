
class FacebookConsumer:

    def __init__(self, api_token):
        self._api_token = api_token

    ...

    def get_lastest_timeline_post(self):
        return self.make_request('some-url')
    ...

class TwitterConsumer:

    def __init__(self, api_token):
        self._api_token = api_token

    ...

    def get_lastest_tweet(self):
        return self.make_request('some-url')
    ...
