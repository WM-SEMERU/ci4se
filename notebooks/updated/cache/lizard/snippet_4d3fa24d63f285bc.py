def encode_string(data, encoding='hex'):
    if six.PY2:
        return data.encode(encoding)
    else:
        if isinstance(data, str):
            data = bytes(data, 'utf-8')
        return codecs.encode(data, encoding).decode('ascii')