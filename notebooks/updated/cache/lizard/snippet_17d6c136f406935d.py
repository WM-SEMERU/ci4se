def reverse_iter(self, start=None, stop=None, count=2000):
    cursor = '0'
    count = 1000
    start = start if start is not None else -1 * count
    stop = stop if stop is not None else -1
    _loads = self._loads
    while cursor:
        cursor = self._client.lrange(self.key_prefix, start, stop)
        for x in reversed(cursor or []):
            yield _loads(x)
        start -= count
        stop -= count