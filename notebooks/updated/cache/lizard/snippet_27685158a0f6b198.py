def get_type(self):
    if self.total_size() == 0:
        return CONSTANT_TYPE_NULL
    return unpack_from(FMT_BE_INT, self._buffer, TYPE_OFFSET)[0]