def get_connection(self, **kwargs):
    if self.is_rtscts():
        return RTSCTSConnection(self, **kwargs)
    if self.is_dsrdtr():
        return DSRDTRConnection(self, **kwargs)
    else:
        raise RuntimeError('Serial protocol "%s" is not available.' % self.
            protocol)