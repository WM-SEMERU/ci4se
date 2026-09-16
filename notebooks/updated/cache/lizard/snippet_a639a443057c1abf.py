def Storage_untrackCacheStorageForOrigin(self, origin):
    assert isinstance(origin, (str,)
        ), "Argument 'origin' must be of type '['str']'. Received type: '%s'" % type(
        origin)
    subdom_funcs = self.synchronous_command(
        'Storage.untrackCacheStorageForOrigin', origin=origin)
    return subdom_funcs