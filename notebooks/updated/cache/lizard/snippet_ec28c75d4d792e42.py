def _ReadEncodedData(self, read_size):
    encoded_data = self._file_object.read(read_size)
    read_count = len(encoded_data)
    self._encoded_data = b''.join([self._encoded_data, encoded_data])
    self._decoded_data, self._encoded_data = self._decoder.Decode(self.
        _encoded_data)
    self._decoded_data_size = len(self._decoded_data)
    return read_count