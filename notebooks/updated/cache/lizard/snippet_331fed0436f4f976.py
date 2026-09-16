def consume_length_prefix(rlp, start):
    b0 = rlp[start]
    if b0 < 128:
        return b'', bytes, 1, start
    elif b0 < SHORT_STRING:
        if b0 - 128 == 1 and rlp[start + 1] < 128:
            raise DecodingError(
                'Encoded as short string although single byte was possible',
                rlp)
        return rlp[start:start + 1], bytes, b0 - 128, start + 1
    elif b0 < 192:
        ll = b0 - 183
        if rlp[start + 1:start + 2] == b'\x00':
            raise DecodingError('Length starts with zero bytes', rlp)
        len_prefix = rlp[start + 1:start + 1 + ll]
        l = big_endian_to_int(len_prefix)
        if l < 56:
            raise DecodingError('Long string prefix used for short string', rlp
                )
        return rlp[start:start + 1] + len_prefix, bytes, l, start + 1 + ll
    elif b0 < 192 + 56:
        return rlp[start:start + 1], list, b0 - 192, start + 1
    else:
        ll = b0 - 192 - 56 + 1
        if rlp[start + 1:start + 2] == b'\x00':
            raise DecodingError('Length starts with zero bytes', rlp)
        len_prefix = rlp[start + 1:start + 1 + ll]
        l = big_endian_to_int(len_prefix)
        if l < 56:
            raise DecodingError('Long list prefix used for short list', rlp)
        return rlp[start:start + 1] + len_prefix, list, l, start + 1 + ll