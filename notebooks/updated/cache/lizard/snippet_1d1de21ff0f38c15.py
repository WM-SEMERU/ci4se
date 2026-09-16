def inv_n(x):
    assert x.ndim == 3
    assert x.shape[1] == x.shape[2]
    c = np.array([[(cofactor_n(x, j, i) * (1 - (i + j) % 2 * 2)) for j in
        range(x.shape[1])] for i in range(x.shape[1])]).transpose(2, 0, 1)
    return c / det_n(x)[:, (np.newaxis), (np.newaxis)]