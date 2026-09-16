def read_raw_temp(self):
    self.i2c.write8(BMP085_CONTROL, BMP085_READTEMPCMD)
    time.sleep(0.005)
    raw = self.i2c.read_U16BE(BMP085_TEMPDATA)
    self.logger.debug('Raw temp 0x{0:X} ({1})', raw & 65535, raw)
    return raw