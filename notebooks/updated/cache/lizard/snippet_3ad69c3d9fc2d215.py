def lha2matrix(values, shape):
    M = np.zeros(shape)
    for v in values:
        M[tuple([int(i - 1) for i in v[:-1]])] = v[-1]
    return M