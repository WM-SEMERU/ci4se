def set_mode(self, gpio, mode):
    res = yield from self._pigpio_aio_command(_PI_CMD_MODES, gpio, mode)
    return _u2i(res)