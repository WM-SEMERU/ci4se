def get_bits_from_int(val_int, val_size=16):
    bits = [None] * val_size
    for i, item in enumerate(bits):
        bits[i] = bool(val_int >> i & 1)
    return bits