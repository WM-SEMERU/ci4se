def _write8(self, reg, value):
    self.i2c.write8(TCS34725_COMMAND_BIT | reg, value)