def despeckle_local(M, stds=2, width=2):
    N = np.array(M, dtype=np.float64)
    n, m = M.shape
    for i, j in itertools.product(range(width, n - width), range(width, m -
        width)):
        square = M[i - width:i + width, j - width:j + width]
        avg = np.average(square)
        std = np.std(square)
        if M[i, j] >= avg + stds * std:
            N[i, j] = avg
    return (N + N.T) / 2