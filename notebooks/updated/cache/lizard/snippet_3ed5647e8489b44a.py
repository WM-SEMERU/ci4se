def _extalg(xarr, alpha=100, axis=None):
    return np.sum(xarr * np.exp(alpha * xarr), axis=axis, keepdims=True
        ) / np.sum(np.exp(alpha * xarr), axis=axis, keepdims=True)