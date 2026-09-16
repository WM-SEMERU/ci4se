def iter_subscriptions(self, login=None, number=-1, etag=None):
    if login:
        return self.user(login).iter_subscriptions()
    url = self._build_url('user', 'subscriptions')
    return self._iter(int(number), url, Repository, etag=etag)