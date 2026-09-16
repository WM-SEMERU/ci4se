def closest_val(x, L):
    if len(L) == 0:
        raise ValueError('L must not be empty')
    if isinstance(L, np.ndarray):
        return np.abs(L - x).argmin()
    min_index = 0
    min_diff = abs(L[0] - x)
    i = 1
    while i < len(L):
        diff = abs(L[i] - x)
        if diff < min_diff:
            min_index = i
            min_diff = diff
        i += 1
    return min_index