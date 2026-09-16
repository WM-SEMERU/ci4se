def batch(self, num):
    self._params.pop('limit', None)
    it = iter(self)
    while True:
        chunk = list(islice(it, num))
        if not chunk:
            return
        yield chunk