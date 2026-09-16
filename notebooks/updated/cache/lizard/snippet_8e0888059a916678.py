def request(self, method, url, **kwargs):
    kwargs['auth'] = self.auth()
    kwargs['cookies'] = self.cookies
    return requests.request(method=method, url=url, **kwargs)