def read(self, length, dummy=None):
    assert not self.closed
    data = self.expected_read_data.pop(0)
    if length < len(data):
        raise ValueError(
            'Overflow packet length. Read %d bytes, got %d bytes: %s',
            length, len(data), self._dotify(data))
    return data