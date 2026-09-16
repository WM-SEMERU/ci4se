def update(self, res, pk, depth=1, since=None):
    fetch = lambda : self._fetcher.fetch_latest(res, pk, 1, since=since)
    self._update(res, fetch, depth)