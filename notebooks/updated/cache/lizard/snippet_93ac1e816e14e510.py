def subscribe_to_hub(self, event, callback, secret=github.GithubObject.NotSet):
    return self._hub('subscribe', event, callback, secret)