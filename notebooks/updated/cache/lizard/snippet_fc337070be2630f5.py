def length_prefix(length, offset):
    if length < 56:
        return ALL_BYTES[offset + length]
    elif length < LONG_LENGTH:
        length_string = int_to_big_endian(length)
        return ALL_BYTES[offset + 56 - 1 + len(length_string)] + length_string
    else:
        raise ValueError('Length greater than 256**8')