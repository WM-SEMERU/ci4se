def decode(self):
    self.blocknumber, = struct.unpack(str('!H'), self.buffer[2:4])
    log.debug('decoding DAT packet, block number %d', self.blocknumber)
    log.debug('should be %d bytes in the packet total', len(self.buffer))
    self.data = self.buffer[4:]
    log.debug('found %d bytes of data', len(self.data))
    return self