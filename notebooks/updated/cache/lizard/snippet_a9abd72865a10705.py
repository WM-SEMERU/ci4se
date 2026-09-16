def _get_generality(key, mask):
    xs = ~key & ~mask
    return sum(1 for i in range(32) if xs & 1 << i)