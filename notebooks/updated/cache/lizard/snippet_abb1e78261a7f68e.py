def read(self, fd):
    args = {'fd': fd}
    data = self._client.json('filesystem.read', args)
    return base64.decodebytes(data.encode())