def version_cmp(version_a, version_b):
    a = normalize_version(version_a)
    b = normalize_version(version_b)
    i_a = a[0] * 100 + a[1] * 10 + a[0] * 1
    i_b = b[0] * 100 + b[1] * 10 + b[0] * 1
    return i_a - i_b