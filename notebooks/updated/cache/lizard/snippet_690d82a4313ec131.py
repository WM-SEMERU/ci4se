def _unparse_attr(self, attr_type, attr_value):
    if self._needs_base64_encoding(attr_type, attr_value):
        if not isinstance(attr_value, bytes):
            attr_value = attr_value.encode(self._encoding)
        encoded = base64.encodestring(attr_value).replace(b'\n', b'').decode(
            'ascii')
        line = ':: '.join([attr_type, encoded])
    else:
        line = ': '.join([attr_type, attr_value])
    self._fold_line(line.encode('ascii'))