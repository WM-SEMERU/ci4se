def backward(A, pobs, T=None, beta_out=None, dtype=np.float32):
    if T is None:
        T = pobs.shape[0]
    elif T > pobs.shape[0]:
        raise ValueError('T must be at most the length of pobs.')
    N = A.shape[0]
    if beta_out is None:
        beta_out = np.zeros((T, N), dtype=dtype)
    elif T > beta_out.shape[0]:
        raise ValueError(
            'beta_out must at least have length T in order to fit trajectory.')
    beta_out[(T - 1), :] = 1.0
    scale = np.sum(beta_out[(T - 1), :])
    beta_out[(T - 1), :] /= scale
    for t in range(T - 2, -1, -1):
        np.dot(A, beta_out[(t + 1), :] * pobs[(t + 1), :], out=beta_out[(t), :]
            )
        scale = np.sum(beta_out[(t), :])
        beta_out[(t), :] /= scale
    return beta_out