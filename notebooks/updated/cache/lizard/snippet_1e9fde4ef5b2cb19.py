def augment_tensor(matrix, ndim=None):
    s = matrix.shape
    if ndim is None:
        ndim = s[0] + 1
    arr = N.identity(ndim)
    arr[:s[0], :s[1]] = matrix
    return arr