def repmat(x, r, c):
    if sps.issparse(x):
        row = sps.hstack([x for _ in range(c)])
        return sps.vstack([row for _ in range(r)], format=x.format)
    else:
        return np.matlib.repmat(x, r, c)