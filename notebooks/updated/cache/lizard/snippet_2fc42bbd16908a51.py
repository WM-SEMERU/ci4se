def set_cached_resource_size(self, resource_name, size):
    size_data = json_dumps({'size': size, 'recorded_time': time()})
    self.cache.set('SIZE:%s' % resource_name, size_data, ex=self.
        size_cache_timeout)
    return