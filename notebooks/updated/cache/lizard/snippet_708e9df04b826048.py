def _eight_byte_real(value):
    if value == 0:
        return b'\x00\x00\x00\x00\x00\x00\x00\x00'
    if value < 0:
        byte1 = 128
        value = -value
    else:
        byte1 = 0
    fexp = numpy.log2(value) / 4
    exponent = int(numpy.ceil(fexp))
    if fexp == exponent:
        exponent += 1
    mantissa = int(value * 16.0 ** (14 - exponent))
    byte1 += exponent + 64
    byte2 = mantissa // 281474976710656
    short3 = mantissa % 281474976710656 // 4294967296
    long4 = mantissa % 4294967296
    return struct.pack('>HHL', byte1 * 256 + byte2, short3, long4)