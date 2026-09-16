def fl2norm2(xf, axis=(0, 1)):
    r
    xfs = xf.shape
    return np.linalg.norm(xf) ** 2 / np.prod(np.array([xfs[k] for k in axis]))