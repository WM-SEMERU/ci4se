def close(self):
    if not self.active:
        return
    self.stop_thread()
    for chan in list(self._channels.values()):
        chan._unlink()
    self.sock.close()