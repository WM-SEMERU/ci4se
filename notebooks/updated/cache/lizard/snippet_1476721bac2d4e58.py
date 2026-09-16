def b2a_base58(s):
    v, prefix = to_long(256, lambda x: x, iterbytes(s))
    s = from_long(v, prefix, BASE58_BASE, lambda v: BASE58_ALPHABET[v])
    return s.decode('utf8')