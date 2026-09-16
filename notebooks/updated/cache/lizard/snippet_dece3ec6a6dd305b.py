def write_padding_bits(buff, version, length):
    if version not in (consts.VERSION_M1, consts.VERSION_M3):
        buff.extend([0] * (8 - length % 8))