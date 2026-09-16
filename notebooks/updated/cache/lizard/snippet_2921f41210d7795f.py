def read_chunked(self, amt=None, decode_content=None):
    self._init_decoder()
    if not self.chunked:
        raise ResponseNotChunked(
            "Response is not chunked. Header 'transfer-encoding: chunked' is missing."
            )
    if not self.supports_chunked_reads():
        raise BodyNotHttplibCompatible(
            'Body should be httplib.HTTPResponse like. It should have have an fp attribute which returns raw chunks.'
            )
    with self._error_catcher():
        if self._original_response and is_response_to_head(self.
            _original_response):
            self._original_response.close()
            return
        if self._fp.fp is None:
            return
        while True:
            self._update_chunk_length()
            if self.chunk_left == 0:
                break
            chunk = self._handle_chunk(amt)
            decoded = self._decode(chunk, decode_content=decode_content,
                flush_decoder=False)
            if decoded:
                yield decoded
        if decode_content:
            decoded = self._flush_decoder()
            if decoded:
                yield decoded
        while True:
            line = self._fp.fp.readline()
            if not line:
                break
            if line == b'\r\n':
                break
        if self._original_response:
            self._original_response.close()