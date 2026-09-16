def command(self, *cmd):
    assert len(cmd) <= 32
    try:
        self._bus.write_i2c_block_data(self._addr, self._cmd_mode, list(cmd))
    except (IOError, OSError) as e:
        if e.errno in [errno.EREMOTEIO, errno.EIO]:
            raise luma.core.error.DeviceNotFoundError(
                'I2C device not found on address: 0x{0:02X}'.format(self._addr)
                )
        else:
            raise