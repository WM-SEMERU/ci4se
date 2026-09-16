def stream(self):
    stream = self._p4dict.get('stream')
    if stream:
        return Stream(stream, self._connection)