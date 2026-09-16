def write(self, data):
    if not isinstance(data, (bytes, bytearray, list)):
        raise TypeError(
            'Invalid data type, should be bytes, bytearray, or list.')
    if isinstance(data, list):
        data = bytearray(data)
    try:
        return os.write(self._fd, data)
    except OSError as e:
        raise SerialError(e.errno, 'Writing serial port: ' + e.strerror)