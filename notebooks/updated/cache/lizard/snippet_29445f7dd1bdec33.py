def is_alive(self):
    null = chr(0)
    try:
        if self.device is None:
            return {'is_alive': False}
        else:
            self._send_command(null)
    except (socket.error, EOFError):
        return {'is_alive': False}
    return {'is_alive': self.device.remote_conn.transport.is_active()}