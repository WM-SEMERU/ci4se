def output(self, stream, disabletransferencoding=None):
    if self._sendHeaders:
        raise HttpProtocolException(
            'Cannot modify response, headers already sent')
    self.outputstream = stream
    try:
        content_length = len(stream)
    except Exception:
        pass
    else:
        self.header(b'Content-Length', str(content_length).encode('ascii'))
    if disabletransferencoding is not None:
        self.disabledeflate = disabletransferencoding
    self._startResponse()