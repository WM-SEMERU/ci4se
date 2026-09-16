def _parse_var_int_components(buf, signed):
    value = 0
    sign = 1
    while True:
        ch = buf.read(1)
        if ch == '':
            raise IonException('Variable integer under-run')
        octet = ord(ch)
        if signed:
            if octet & _VAR_INT_SIGN_MASK:
                sign = -1
            value = octet & _VAR_INT_SIGN_VALUE_MASK
            signed = False
        else:
            value <<= _VAR_INT_VALUE_BITS
            value |= octet & _VAR_INT_VALUE_MASK
        if octet & _VAR_INT_SIGNAL_MASK:
            break
    return sign, value