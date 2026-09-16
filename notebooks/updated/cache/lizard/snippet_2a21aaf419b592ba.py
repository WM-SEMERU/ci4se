def _request(self, url, **kwargs):
    if self.method is None:
        raise NotImplementedError('method must be defined on a subclass')
    response = requests.request(self.method, url, **kwargs)
    return self.response_class(response, sender=self)