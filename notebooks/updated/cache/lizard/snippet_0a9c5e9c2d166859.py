def get(self, channel):
    checked_channel = self._check_channel_no(channel)
    self.i2c.write_raw8(checked_channel | self._dac_enabled)
    reading = self.i2c.read_raw8()
    reading = self.i2c.read_raw8()
    return reading / 255.0