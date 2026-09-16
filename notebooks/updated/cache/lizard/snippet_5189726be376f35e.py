def ibm_to_ieee(ibm):
    ibm = ibm.ljust(8, b'\x00')
    ulong, = struct.unpack('>Q', ibm)
    sign = ulong & 9223372036854775808
    exponent = (ulong & 9151314442816847872) >> 56
    mantissa = ulong & 72057594037927935
    if mantissa == 0:
        if ibm[0:1] == b'\x00':
            return 0.0
        elif ibm[0:1] in b'_.ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return float('nan')
        else:
            raise ValueError('Neither zero nor NaN: %r' % ibm)
    if ulong & 36028797018963968:
        shift = 3
    elif ulong & 18014398509481984:
        shift = 2
    elif ulong & 9007199254740992:
        shift = 1
    else:
        shift = 0
    mantissa >>= shift
    mantissa &= 18442240474082181119
    exponent -= 65
    exponent <<= 2
    exponent += shift + 1023
    ieee = sign | exponent << 52 | mantissa
    return struct.unpack('>d', struct.pack('>Q', ieee))[0]