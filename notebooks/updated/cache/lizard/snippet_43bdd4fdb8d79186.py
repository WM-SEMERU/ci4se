def make_subdivision_matrices(degree):
    left = np.zeros((degree + 1, degree + 1), order='F')
    right = np.zeros((degree + 1, degree + 1), order='F')
    left[0, 0] = 1.0
    right[-1, -1] = 1.0
    for col in six.moves.xrange(1, degree + 1):
        half_prev = 0.5 * left[:col, (col - 1)]
        left[:col, (col)] = half_prev
        left[1:col + 1, (col)] += half_prev
        complement = degree - col
        right[-(col + 1):, (complement)] = left[:col + 1, (col)]
    return left, right