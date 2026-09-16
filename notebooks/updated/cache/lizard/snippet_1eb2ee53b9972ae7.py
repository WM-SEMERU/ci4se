def _send_cmd(self, cmd: str):
    self._sock.sendall(cmd.encode(encoding='latin-1', errors='strict'))