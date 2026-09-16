def BatchNorm(x, params, axis=(0, 1, 2), epsilon=1e-05, center=True, scale=
    True, **unused_kwargs):
    mean = np.mean(x, axis, keepdims=True)
    m1 = np.mean(x ** 2, axis, keepdims=True)
    var = m1 - mean ** 2
    z = (x - mean) / np.sqrt(var + epsilon)
    beta, gamma = params
    ed = tuple(None if i in axis else slice(None) for i in range(np.ndim(x)))
    beta = beta[ed]
    gamma = gamma[ed]
    if center and scale:
        return gamma * z + beta
    if center:
        return z + beta
    if scale:
        return gamma * z
    return z