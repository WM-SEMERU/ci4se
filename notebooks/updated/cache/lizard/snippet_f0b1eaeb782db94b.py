def close(self):
    self.stop_sync()
    [c.io.close() for c in self._controllers if c.io is not None]