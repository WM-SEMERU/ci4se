def connect(self):
    self._start_connect(self.CA_SINGLE_SHOT)
    while (self._connect_state.value == self.CS_ATTEMPTING_CONNECT or self.
        _connect_state.value == self.CS_CONNECTING):
        time.sleep(0.1)
    if self.CS_CONNECTED != self._connect_state.value:
        raise exceptions.RoasterLookupError