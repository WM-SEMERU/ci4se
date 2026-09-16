def _stop_transmit(self, stream):
    _vv and IOLOG.debug('%r._stop_transmit(%r)', self, stream)
    self.poller.stop_transmit(stream.transmit_side.fd)