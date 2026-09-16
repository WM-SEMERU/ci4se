def disconnect(self):
    if not self.connected:
        raise HardwareError('Cannot disconnect when we are not connected')
    self._reports = None
    self._traces = None
    self._loop.run_coroutine(self.adapter.disconnect(0))
    self.connected = False
    self.connection_interrupted = False
    self.connection_string = None