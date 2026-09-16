def read_chunk_header(self):
    try:
        chunk_size_hex = yield from self._connection.readline()
    except ValueError as error:
        raise ProtocolError('Invalid chunk size: {0}'.format(error)) from error
    if not chunk_size_hex.endswith(b'\n'):
        raise NetworkError('Connection closed.')
    try:
        chunk_size = int(chunk_size_hex.split(b';', 1)[0].strip(), 16)
    except ValueError as error:
        raise ProtocolError('Invalid chunk size: {0}'.format(error)) from error
    if chunk_size < 0:
        raise ProtocolError('Chunk size cannot be negative.')
    self._chunk_size = self._bytes_left = chunk_size
    return chunk_size, chunk_size_hex