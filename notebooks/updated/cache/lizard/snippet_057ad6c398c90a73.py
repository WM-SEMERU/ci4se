def _read_values(self, file, number_values):
    if self.data_type.nptype is not None:
        dtype = np.dtype(self.data_type.nptype).newbyteorder(self.endianness)
        return fromfile(file, dtype=dtype, count=number_values)
    elif self.data_type == types.String:
        return read_string_data(file, number_values, self.endianness)
    data = self._new_segment_data()
    for i in range(number_values):
        data[i] = self.data_type.read(file, self.endianness)
    return data