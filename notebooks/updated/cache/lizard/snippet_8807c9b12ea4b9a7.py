def write(self, gpio, level):
    res = yield from self._pigpio_aio_command(_PI_CMD_WRITE, gpio, level)
    return _u2i(res)