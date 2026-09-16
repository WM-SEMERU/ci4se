def decode_data(self, data):
    assert self.get_empty() is False
    assert self._data_encoded is True
    if self._block_allowed:
        data = self._decode_transfer_block_data(data)
    else:
        data = self._decode_transfer_data(data)
    return data