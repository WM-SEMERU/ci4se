def unpack_remb_fci(data):
    if len(data) < 8 or data[0:4] != b'REMB':
        raise ValueError('Invalid REMB prefix')
    exponent = (data[5] & 252) >> 2
    mantissa = (data[5] & 3) << 16 | data[6] << 8 | data[7]
    bitrate = mantissa << exponent
    pos = 8
    ssrcs = []
    for r in range(data[4]):
        ssrcs.append(unpack_from('!L', data, pos)[0])
        pos += 4
    return bitrate, ssrcs