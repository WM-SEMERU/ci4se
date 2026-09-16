def encodeLength(length):
    if length < 128:
        ored_length = length
        offset = -1
    elif length < 16384:
        ored_length = length | 32768
        offset = -2
    elif length < 2097152:
        ored_length = length | 12582912
        offset = -3
    elif length < 268435456:
        ored_length = length | 3758096384
        offset = -4
    else:
        raise ConnectionError('Unable to encode length of {}'.format(length))
    return pack('!I', ored_length)[offset:]