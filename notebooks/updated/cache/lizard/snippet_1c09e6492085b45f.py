def _convert_public_key(ecdsa_curve_name, result):
    if ecdsa_curve_name == 'nist256p1':
        if result[64] & 1 != 0:
            result = bytearray([3]) + result[1:33]
        else:
            result = bytearray([2]) + result[1:33]
    else:
        result = result[1:]
        keyX = bytearray(result[0:32])
        keyY = bytearray(result[32:][::-1])
        if keyX[31] & 1 != 0:
            keyY[31] |= 128
        result = b'\x00' + bytes(keyY)
    return bytes(result)