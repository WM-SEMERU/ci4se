def _readStreamHeader(self):
    magic, version = self._readStruct('>HH')
    if magic != self.STREAM_MAGIC or version != self.STREAM_VERSION:
        raise IOError(
            'The stream is not java serialized object. Invalid stream header: {0:04X}{1:04X}'
            .format(magic, version))