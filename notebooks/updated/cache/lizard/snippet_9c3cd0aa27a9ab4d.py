def next(self):
    self.open_read()
    data = self.resp.read(self.BufferSize)
    if not data:
        self.close()
        raise StopIteration
    return data