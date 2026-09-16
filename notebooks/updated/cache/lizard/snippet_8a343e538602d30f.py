def lrange(self, key, start, stop):
    redis_list = self._get_list(key, 'LRANGE')
    start, stop = self._translate_range(len(redis_list), start, stop)
    return redis_list[start:stop + 1]