def purge(self):
    while not self.stopped.isSet():
        self.stopped.wait(timeout=defines.EXCHANGE_LIFETIME)
        self._messageLayer.purge()