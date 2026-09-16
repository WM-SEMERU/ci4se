def set_gain(self, gain=1):
    if gain == 1:
        self.i2c.write8(129, 2)
    else:
        self.i2c.write8(129, 18)
    time.sleep(self.pause)