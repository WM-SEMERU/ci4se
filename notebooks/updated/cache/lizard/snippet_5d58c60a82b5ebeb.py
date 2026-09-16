def mean_first_passage_time(adjacency):
    P = np.linalg.solve(np.diag(np.sum(adjacency, axis=1)), adjacency)
    n = len(P)
    D, V = np.linalg.eig(P.T)
    aux = np.abs(D - 1)
    index = np.where(aux == aux.min())[0]
    if aux[index] > 0.01:
        raise ValueError('Cannot find eigenvalue of 1. Minimum eigenvalue ' +
            'value is {0}. Tolerance was '.format(aux[index] + 1) +
            'set at 10e-3.')
    w = V[:, (index)].T
    w = w / np.sum(w)
    W = np.real(np.repeat(w, n, 0))
    I = np.eye(n)
    Z = np.linalg.inv(I - P + W)
    mfpt = (np.repeat(np.atleast_2d(np.diag(Z)), n, 0) - Z) / W
    return mfpt