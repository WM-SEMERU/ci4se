def CacheStorage_deleteEntry(self, cacheId, request):
    assert isinstance(request, (str,)
        ), "Argument 'request' must be of type '['str']'. Received type: '%s'" % type(
        request)
    subdom_funcs = self.synchronous_command('CacheStorage.deleteEntry',
        cacheId=cacheId, request=request)
    return subdom_funcs