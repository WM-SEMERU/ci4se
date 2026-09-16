def distance_law(matrix, log_bins=False):
    D = np.array([np.average(np.diagonal(matrix, j)) for j in range(min(
        matrix.shape))])
    if not log_bins:
        return D
    else:
        n = min(matrix.shape)
        n_bins = int(np.log(n) / np.log(2) + 1)
        logD = np.array([np.average(D[int(2 ** (i - 1)):min(n, 2 ** i)]) for
            i in range(n_bins)])
        return logD