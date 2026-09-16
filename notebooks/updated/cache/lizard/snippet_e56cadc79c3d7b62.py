def state(self, *args, **kwargs):
    return self._makeApiCall(self.funcinfo['state'], *args, **kwargs)