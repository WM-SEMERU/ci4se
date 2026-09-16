def _readall(self, file, count):
    data = b''
    while len(data) < count:
        d = file.read(count - len(data))
        if not d:
            raise GeneralProxyError('Connection closed unexpectedly')
        data += d
    return data