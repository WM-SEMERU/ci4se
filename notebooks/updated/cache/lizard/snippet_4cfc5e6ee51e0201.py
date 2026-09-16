def put(self, bytes):
    key = self.get_key_from_request()
    result_ttl = self.get_max_age()
    logger.debug('[REDIS_RESULT_STORAGE] putting `{key}` with ttl `{ttl}`'.
        format(key=key, ttl=result_ttl))
    storage = self.get_storage()
    storage.set(key, bytes)
    if result_ttl > 0:
        storage.expireat(key, datetime.now() + timedelta(seconds=result_ttl))
    return key