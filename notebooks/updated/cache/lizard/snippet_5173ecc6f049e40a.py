def software_reset(i2c=None, **kwargs):
    if i2c is None:
        import Adafruit_GPIO.I2C as I2C
        i2c = I2C
    self._device = i2c.get_i2c_device(0, **kwargs)
    self._device.writeRaw8(6)