def cache(self, resource):
    if not isinstance(resource, APIResource):
        raise TypeError(
            'Cannot cache `{!r}`, can only cache APIResource instances'.
            format(resource))
    if self.__cache_max_size == 0:
        return
    try:
        cache_internal_key = resource.get_cache_internal_key()
        cache_index_keys = resource.get_cache_index_keys().items()
    except NotImplementedError:
        logger.warning(
            'Not caching `{!r}`, resource did not provide all necessary cache details'
            .format(resource))
    else:
        resource_type = type(resource)
        for key, value in cache_index_keys:
            self.__cache_index_key_map[resource_type, key, value
                ] = cache_internal_key
        self.__caches[resource_type][cache_internal_key] = resource
        logger.debug('Cached `{!r}`'.format(resource))