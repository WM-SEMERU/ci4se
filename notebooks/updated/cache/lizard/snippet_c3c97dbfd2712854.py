def Split(axis, a, n):
    return tuple(np.split(np.copy(a), n, axis=axis))