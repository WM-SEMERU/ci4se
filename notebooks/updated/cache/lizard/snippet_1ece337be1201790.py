def script_status(self, script_id):
    res = yield from self._pigpio_aio_command(_PI_CMD_PROCP, script_id, 0)
    bytes = u2i(res)
    if bytes > 0:
        data = yield from self._loop.sock_recv(self.s, bytes)
        while len(data) < bytes:
            b = yield from self._loop.sock_recv(self.s, bytes - len(data))
            data.extend(b)
        pars = struct.unpack('11i', _str(data))
        status = pars[0]
        params = pars[1:]
    else:
        status = bytes
        params = ()
    return status, params