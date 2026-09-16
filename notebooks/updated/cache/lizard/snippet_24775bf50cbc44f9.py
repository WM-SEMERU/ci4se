def delete(self, *raw_args, **raw_kwargs):
    args = self.prepare_args(*raw_args)
    kwargs = self.prepare_kwargs(**raw_kwargs)
    key = self.key(*args, **kwargs)
    item = self.cache.get(key)
    if item is not None:
        self.cache.delete(key)