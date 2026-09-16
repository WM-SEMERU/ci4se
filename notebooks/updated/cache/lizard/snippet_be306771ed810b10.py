def set_range(self, accel=1, gyro=1):
    self.i2c_write_register(28, accel)
    self.i2c_write_register(27, gyro)
    self.accel_range = accel
    self.gyro_range = gyro