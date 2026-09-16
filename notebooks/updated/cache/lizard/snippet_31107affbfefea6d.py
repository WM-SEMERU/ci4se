def get_adjacent_index(I, shape, size):
    m, n = shape
    In = I % n
    bL = In != 0
    bR = In != n - 1
    J = np.concatenate([I - n, I[bL] - 1, I[bR] + 1, I + n, I[bL] - n - 1, 
        I[bR] - n + 1, I[bL] + n - 1, I[bR] + n + 1])
    J = J[(J >= 0) & (J < size)]
    return J