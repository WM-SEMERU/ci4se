def i2c_master_write_read(self, i2c_address, data, length):
    self.i2c_master_write(i2c_address, data, I2C_NO_STOP)
    return self.i2c_master_read(i2c_address, length)