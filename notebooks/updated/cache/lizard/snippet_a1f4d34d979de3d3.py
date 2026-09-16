def _required_byte_num(mode, fmt, n_samp):
    if fmt == '212':
        n_bytes = math.ceil(n_samp * 1.5)
    elif fmt in ['310', '311']:
        n_extra = n_samp % 3
        if n_extra == 2:
            if fmt == '310':
                n_bytes = upround(n_samp * 4 / 3, 4)
            elif mode == 'read':
                n_bytes = math.ceil(n_samp * 4 / 3)
            else:
                n_bytes = upround(n_samp * 4 / 3, 4)
        else:
            n_bytes = math.ceil(n_samp * 4 / 3)
    else:
        n_bytes = n_samp * BYTES_PER_SAMPLE[fmt]
    return int(n_bytes)