def cache_key(self, request, method=None):
    if method is None:
        method = request.method
    return 'bettercache_page:%s:%s' % (request.build_absolute_uri(), method)