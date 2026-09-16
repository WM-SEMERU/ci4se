def get_common_xs(entries):
    key = 0
    mask = 0
    for entry in entries:
        key |= entry.key
        mask |= entry.mask
    return ~(key | mask) & 4294967295