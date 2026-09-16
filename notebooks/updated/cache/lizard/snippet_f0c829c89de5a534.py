def ServiceWorker_inspectWorker(self, versionId):
    assert isinstance(versionId, (str,)
        ), "Argument 'versionId' must be of type '['str']'. Received type: '%s'" % type(
        versionId)
    subdom_funcs = self.synchronous_command('ServiceWorker.inspectWorker',
        versionId=versionId)
    return subdom_funcs