def clone(self):
    return Timeout(connect=self._connect, read=self._read, total=self.total)