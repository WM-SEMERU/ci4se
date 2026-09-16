def stream_keepalive(self, listenKey):
    params = {'listenKey': listenKey}
    return self._put('userDataStream', False, data=params)