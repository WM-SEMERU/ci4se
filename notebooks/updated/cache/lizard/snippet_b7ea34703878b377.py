def open(self):
    self._inbound = []
    self._exceptions = []
    self.set_state(self.OPENING)
    self.rpc_request(specification.Channel.Open())
    self.set_state(self.OPEN)