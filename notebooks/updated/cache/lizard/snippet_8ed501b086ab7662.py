def create(options, timer=None, use_deque=True):
    if options is None:
        return None
    if not isinstance(options, (CheckOptions, QuotaOptions, ReportOptions)):
        _logger.error('make_cache(): bad options %s', options)
        raise ValueError('Invalid options')
    if options.num_entries <= 0:
        _logger.debug('did not create cache, options was %s', options)
        return None
    _logger.debug('creating a cache from %s', options)
    if options.flush_interval > ZERO_INTERVAL:
        ttl = getattr(options, 'expiration', options.flush_interval)
        cache_cls = DequeOutTTLCache if use_deque else cachetools.TTLCache
        return LockedObject(cache_cls(options.num_entries, ttl=ttl.
            total_seconds(), timer=to_cache_timer(timer)))
    cache_cls = DequeOutLRUCache if use_deque else cachetools.LRUCache
    return LockedObject(cache_cls(options.num_entries))