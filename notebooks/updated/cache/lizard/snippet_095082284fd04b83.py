def ServiceWorker_stopWorker(self, versionId):
    assert isinstance(versionId, (str,)
        ), "Argument 'versionId' must be of type '['str']'. Received type: '%s'" % type(
        versionId)
    subdom_funcs = self.synchronous_command('ServiceWorker.stopWorker',
        versionId=versionId)
    return subdom_funcs