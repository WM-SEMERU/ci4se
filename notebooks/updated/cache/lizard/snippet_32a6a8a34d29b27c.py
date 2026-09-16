def _read_bytes(self, b):
    if hasattr(self, 'footer'):
        _LOGGER.debug('Source stream processing complete')
        return
    buffer_length = len(self.output_buffer)
    if 0 <= b <= buffer_length:
        _LOGGER.debug(
            '%d bytes requested less than or equal to current output buffer size %d'
            , b, buffer_length)
        return
    if self._header.content_type == ContentType.FRAMED_DATA:
        self.output_buffer += self._read_bytes_from_framed_body(b)
    elif self._header.content_type == ContentType.NO_FRAMING:
        self.output_buffer += self._read_bytes_from_non_framed_body(b)
    else:
        raise NotSupportedError('Unsupported content type')