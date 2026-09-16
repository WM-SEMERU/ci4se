def clear(self, match='*', count=1000):
    cursor = '0'
    pipe = self._client.pipeline(transaction=False)
    while cursor != 0:
        cursor, keys = self.scan(cursor=cursor, match=match, count=count)
        if keys:
            pipe.delete(*keys)
    pipe.hdel(self._bucket_key, self.key_prefix)
    pipe.execute()
    return True