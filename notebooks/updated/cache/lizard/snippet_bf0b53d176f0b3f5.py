def _rle_decode(data):
    if not data:
        return data
    new = b''
    last = b''
    for cur in data:
        if last == b'\x00':
            new += last * cur
            last = b''
        else:
            new += last
            last = bytes([cur])
    return new + last