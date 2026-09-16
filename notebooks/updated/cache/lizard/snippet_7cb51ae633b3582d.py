def read_at(self, offset, to_read, timeout_ms):
    if not isinstance(offset, baseinteger):
        raise TypeError('offset can only be an instance of type baseinteger')
    if not isinstance(to_read, baseinteger):
        raise TypeError('to_read can only be an instance of type baseinteger')
    if not isinstance(timeout_ms, baseinteger):
        raise TypeError(
            'timeout_ms can only be an instance of type baseinteger')
    data = self._call('readAt', in_p=[offset, to_read, timeout_ms])
    return data