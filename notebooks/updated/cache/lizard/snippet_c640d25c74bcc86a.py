def listClients(self, *args, **kwargs):
    return self._makeApiCall(self.funcinfo['listClients'], *args, **kwargs)