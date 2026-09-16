def _put(self, *args, **kwargs):
    if 'timeout' not in kwargs:
        kwargs['timeout'] = self.timeout
    req = self.session.put(*args, **kwargs)
    return req