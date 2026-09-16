def repr_size(n_bytes):
    if n_bytes < 1024:
        return '{0} Bytes'.format(n_bytes)
    i = -1
    while n_bytes > 1023:
        n_bytes /= 1024.0
        i += 1
    return '{0} {1}iB'.format(round(n_bytes, 1), si_prefixes[i])