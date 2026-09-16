def write_raw_byte(self, value):
    self.bus.write_byte(self.address, value)
    self.log.debug('write_raw_byte: Wrote 0x%02X' % value)