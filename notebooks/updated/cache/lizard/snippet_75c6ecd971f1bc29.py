def getbyuuid(self, uuid):
    if uuid not in self._schbyuuid:
        raise KeyError('uuid {0} not registered'.format(uuid))
    return self._schbyuuid[uuid]