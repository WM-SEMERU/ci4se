def body(self):
    if not self._auto_decode:
        return self._body
    if 'body' in self._decode_cache:
        return self._decode_cache['body']
    body = try_utf8_decode(self._body)
    self._decode_cache['body'] = body
    return body