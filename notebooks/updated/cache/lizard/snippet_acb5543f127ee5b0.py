def getHostDetailsByIndex(self, index, lanInterfaceId=1, timeout=1):
    namespace = Lan.getServiceType('getHostDetailsByIndex') + str(
        lanInterfaceId)
    uri = self.getControlURL(namespace)
    results = self.execute(uri, namespace, 'GetGenericHostEntry', timeout=
        timeout, NewIndex=index)
    return HostDetails(results)