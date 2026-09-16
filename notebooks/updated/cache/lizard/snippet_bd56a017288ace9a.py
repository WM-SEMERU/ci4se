def getRemoteObject(self, busName, objectPath, interfaces=None,
    replaceKnownInterfaces=False):
    return self.objHandler.getRemoteObject(busName, objectPath, interfaces,
        replaceKnownInterfaces)