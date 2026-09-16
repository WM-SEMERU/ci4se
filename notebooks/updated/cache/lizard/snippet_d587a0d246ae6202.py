def _eight_byte_real_to_float(value):
    short1, short2, long3 = struct.unpack('>HHL', value)
    exponent = (short1 & 32512) // 256 - 64
    mantissa = (((short1 & 255) * 65536 + short2) * 4294967296 + long3
        ) / 7.205759403792794e+16
    if short1 & 32768:
        return -mantissa * 16.0 ** exponent
    return mantissa * 16.0 ** exponent