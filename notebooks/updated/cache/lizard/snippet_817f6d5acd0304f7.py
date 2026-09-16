def _write_base(buf, value, bits_per_octet, end_bit=0, sign_bit=0,
    is_signed=False):
    if value == 0:
        buf.append(sign_bit | end_bit)
        return 1
    num_bits = bit_length(value)
    num_octets = num_bits // bits_per_octet
    remainder = num_bits % bits_per_octet
    if remainder != 0 or is_signed:
        num_octets += 1
    else:
        remainder = bits_per_octet
    for i in range(num_octets):
        octet = 0
        if i == 0:
            octet |= sign_bit
        if i == num_octets - 1:
            octet |= end_bit
        octet |= value >> num_bits - (remainder + bits_per_octet * i
            ) & _OCTET_MASKS[bits_per_octet]
        buf.append(octet)
    return num_octets