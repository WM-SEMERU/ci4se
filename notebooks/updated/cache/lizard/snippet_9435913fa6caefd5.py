def _read_response(self):
    result = self.buf.read_line().decode('utf-8')
    if not result:
        raise NoResponseError('No response received from server.')
    msg = self._read_message()
    if result != 'ok':
        raise InvalidResponseError(msg)
    return msg