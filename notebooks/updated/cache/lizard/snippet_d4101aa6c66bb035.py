def _K(m):
    M = m * (m - 1) // 2
    K = np.zeros((M, m ** 2), dtype=np.int64)
    row = 0
    for j in range(1, m):
        col = (j - 1) * m + j
        s = m - j
        K[row:row + s, col:col + s] = np.eye(s)
        row += s
    return K