def CacheStorage_requestCachedResponse(self, cacheId, requestURL):
    assert isinstance(requestURL, (str,)
        ), "Argument 'requestURL' must be of type '['str']'. Received type: '%s'" % type(
        requestURL)
    subdom_funcs = self.synchronous_command(
        'CacheStorage.requestCachedResponse', cacheId=cacheId, requestURL=
        requestURL)
    return subdom_funcs