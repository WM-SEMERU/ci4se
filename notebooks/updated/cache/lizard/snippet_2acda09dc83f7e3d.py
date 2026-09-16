def decodeLength(length):
    bytes_length = len(length)
    if bytes_length < 2:
        offset = b'\x00\x00\x00'
        XOR = 0
    elif bytes_length < 3:
        offset = b'\x00\x00'
        XOR = 32768
    elif bytes_length < 4:
        offset = b'\x00'
        XOR = 12582912
    elif bytes_length < 5:
        offset = b''
        XOR = 3758096384
    else:
        raise ConnectionError('Unable to decode length of {}'.format(length))
    decoded = unpack('!I', offset + length)[0]
    decoded ^= XOR
    return decoded