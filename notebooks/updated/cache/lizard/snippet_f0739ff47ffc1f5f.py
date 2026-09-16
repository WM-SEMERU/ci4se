def add(self, data):
    if len(self) + len(data) > self.sizelimit:
        raise OmapiSizeLimitError()
    self.buff.write(data)
    return self