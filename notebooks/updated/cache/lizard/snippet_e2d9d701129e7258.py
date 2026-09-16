def constant_time_cmp(a, b):
    result = True
    for x, y in zip(a, b):
        result &= x == y
    return result