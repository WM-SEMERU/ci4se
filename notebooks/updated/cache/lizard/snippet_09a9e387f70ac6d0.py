def owner(self):
    if self._writer is not None:
        return self.WRITER
    if self._readers:
        return self.READER
    return None