def run(self, callback=None, limit=0):
    if self._handle is None:
        raise self.DeviceIsNotOpen()
    self._callback = callback
    wtypes.pcap_loop(self._handle, limit, self._callback_wrapper, None)