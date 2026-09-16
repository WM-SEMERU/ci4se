def query(self, key=None, **tags):
    args = {'key': key, 'tags': tags}
    self._query_chk.check(args)
    return self._client.json('aggregator.query', args)