def exists(self):
    r = self._client._redis
    flag = '{}:flag'.format(self._queue)
    return bool(r.exists(flag))