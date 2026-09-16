def clear(self, event, ts=None):
    return self.r.delete(self._keygen(event, ts))