def ServiceWorker_unregister(self, scopeURL):
    assert isinstance(scopeURL, (str,)
        ), "Argument 'scopeURL' must be of type '['str']'. Received type: '%s'" % type(
        scopeURL)
    subdom_funcs = self.synchronous_command('ServiceWorker.unregister',
        scopeURL=scopeURL)
    return subdom_funcs