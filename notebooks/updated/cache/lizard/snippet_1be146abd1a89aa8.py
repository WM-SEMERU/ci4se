def replace_surrogate_encode(mystring, exc):
    decoded = []
    for ch in mystring:
        code = ord(ch)
        if not 55296 <= code <= 56575:
            raise exc
        if 56320 <= code <= 56447:
            decoded.append(_unichr(code - 56320))
        elif code <= 56575:
            decoded.append(_unichr(code - 56320))
        else:
            raise NotASurrogateError
    return str().join(decoded)