def data_size(self):
    if is_container(self._data):
        byte_length, bit_length = self._data.container_size()
        return byte_length + math.ceil(bit_length / 8)
    elif is_field(self._data):
        return math.ceil(self._data.bit_size / 8)
    else:
        return 0