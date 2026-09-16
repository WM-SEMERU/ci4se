def cleanup(self):
    self.num_puts = 0
    cached = []
    for i, url_data in enumerate(self.queue):
        key = url_data.cache_url
        cache = url_data.aggregate.result_cache
        if cache.has_result(key):
            cached.append(i)
    for pos in cached:
        self._move_to_top(pos)