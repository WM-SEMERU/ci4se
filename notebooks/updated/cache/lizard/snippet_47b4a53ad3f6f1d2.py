def invalidate(self, *raw_args, **raw_kwargs):
    args = self.prepare_args(*raw_args)
    kwargs = self.prepare_kwargs(**raw_kwargs)
    key = self.key(*args, **kwargs)
    item = self.cache.get(key)
    if item is not None:
        expiry, data = item
        self.store(key, self.timeout(*args, **kwargs), data)
        self.async_refresh(*args, **kwargs)