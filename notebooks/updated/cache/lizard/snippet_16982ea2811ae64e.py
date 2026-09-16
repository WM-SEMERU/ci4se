def addr(self, address):
    if isinstance(address, basestring):
        addr = address.split()
    else:
        addr = list(address)
    for i in xrange(len(addr)):
        if isinstance(addr[i], basestring):
            addr[i] = int(addr[i], 16)
    for frame in self.raw_frames:
        if frame['addr'] == address:
            return frame