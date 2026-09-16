def startLoop(self, useDriverLoop=True):
    if self._inLoop:
        raise RuntimeError('run loop already started')
    self._inLoop = True
    self._driverLoop = useDriverLoop
    self.proxy.startLoop(self._driverLoop)