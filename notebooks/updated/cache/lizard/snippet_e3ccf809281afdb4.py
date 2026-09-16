def _exec_command(self, cmd):
    _, out, err = self._client.exec_command(cmd, timeout=self._timeout)
    return out.read().strip() if not err.read().strip() else None