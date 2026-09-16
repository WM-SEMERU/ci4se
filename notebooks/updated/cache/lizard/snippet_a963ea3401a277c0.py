def size_in_bytes(self, offset, timestamp, key, value, headers=None):
    assert not headers, 'Headers not supported in v0/v1'
    magic = self._magic
    return self.LOG_OVERHEAD + self.record_size(magic, key, value)