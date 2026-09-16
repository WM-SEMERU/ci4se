def finish(self):
    assert lib.BrotliDecoderHasMoreOutput(self._decoder) == lib.BROTLI_FALSE
    if lib.BrotliDecoderIsFinished(self._decoder) == lib.BROTLI_FALSE:
        raise Error('Decompression error: incomplete compressed stream.')
    return b''