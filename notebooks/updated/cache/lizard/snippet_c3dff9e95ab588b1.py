def stop_receive(self, stream):
    _vv and IOLOG.debug('%r.stop_receive(%r)', self, stream)
    self.defer(self.poller.stop_receive, stream.receive_side.fd)