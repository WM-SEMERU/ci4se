def content(self):
    if self._content is not None:
        return self._content
    if self._content_consumed:
        raise RuntimeError('The content for this response was already consumed'
            )
    try:
        self._content = self.raw.read()
    except AttributeError:
        return None
    if 'gzip' in self.headers.get('content-encoding', ''):
        try:
            self._content = decode_gzip(self._content)
        except zlib.error:
            pass
    if self.config.get('decode_unicode'):
        self._content = get_unicode_from_response(self)
    self._content_consumed = True
    return self._content