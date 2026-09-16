def read_byte_data(self, i2c_addr, register, force=None):
    self._set_address(i2c_addr, force=force)
    msg = i2c_smbus_ioctl_data.create(read_write=I2C_SMBUS_READ, command=
        register, size=I2C_SMBUS_BYTE_DATA)
    ioctl(self.fd, I2C_SMBUS, msg)
    return msg.data.contents.byte