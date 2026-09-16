def inline(text, data=None):
    if not data:
        data = text.encode('utf-8')
    elif not isinstance(data, (bytes, bytearray, memoryview)):
        data = str(data).encode('utf-8')
    if len(data) > 64:
        raise ValueError('Too many bytes for the data')
    return types.KeyboardButtonCallback(text, data)