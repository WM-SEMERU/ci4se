def product(*arrays):
    arrays = [np.asarray(x) for x in arrays]
    shape = (len(x) for x in arrays)
    dtype = arrays[0].dtype
    ix = np.indices(shape)
    ix = ix.reshape(len(arrays), -1).T
    out = np.empty_like(ix, dtype=dtype)
    for n, _ in enumerate(arrays):
        out[:, (n)] = arrays[n][ix[:, (n)]]
    return out