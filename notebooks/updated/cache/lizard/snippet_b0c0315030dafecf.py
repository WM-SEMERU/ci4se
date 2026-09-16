def unicode_http_header(value):
    r
    if six.PY3:
        if isinstance(value, six.binary_type):
            value = value.decode()
    return ''.join([(six.text_type(s, e or 'iso-8859-1') if not isinstance(
        s, six.text_type) else s) for s, e in decode_header(value)])