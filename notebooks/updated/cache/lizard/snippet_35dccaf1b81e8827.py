def create(self, alias=None, cache=None, **kwargs):
    if alias:
        config = self.get_alias_config(alias)
    elif cache:
        warnings.warn(
            "Creating a cache with an explicit config is deprecated, use 'aiocache.Cache'"
            , DeprecationWarning)
        config = {'cache': cache}
    else:
        raise TypeError('create call needs to receive an alias or a cache')
    cache = _create_cache(**{**config, **kwargs})
    return cache