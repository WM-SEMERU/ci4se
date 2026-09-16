def bytes_base64(x):
    if six.PY2:
        return base64.encodestring(x).replace('\n', '')
    return base64.encodebytes(bytes_encode(x)).replace(b'\n', b'')