def todict(self):
    r = {}
    r.update(self._buf)
    if self.start_addr:
        r['start_addr'] = self.start_addr
    return r