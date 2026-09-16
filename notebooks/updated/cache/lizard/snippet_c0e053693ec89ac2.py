def u64_to_hex16le(val):
    return ''.join('%02x' % (x & 255) for x in (val, val >> 8, val >> 16, 
        val >> 24, val >> 32, val >> 40, val >> 48, val >> 56))