def reduced_to_matrix(shape, degree, vals_by_weight):
    r
    result = np.empty(shape, order='F')
    index = 0
    for k in six.moves.xrange(degree + 1):
        for j in six.moves.xrange(degree + 1 - k):
            i = degree - j - k
            key = (0,) * i + (1,) * j + (2,) * k
            result[:, (index)] = vals_by_weight[key][:, (0)]
            index += 1
    return result