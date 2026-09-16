def on_receive(self, broker):
    _vv and IOLOG.debug('%r.on_receive()', self)
    buf = self.receive_side.read()
    if not buf:
        return self.on_disconnect(broker)
    self._internal_receive(broker, buf)