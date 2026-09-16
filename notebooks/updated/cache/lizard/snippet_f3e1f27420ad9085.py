def store_script(self, script):
    if len(script):
        res = yield from self._pigpio_aio_command_ext(_PI_CMD_PROC, 0, 0,
            len(script), [script])
        return _u2i(res)
    else:
        return 0