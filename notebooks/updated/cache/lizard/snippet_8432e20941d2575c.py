def one_hot(x, size, dtype=np.float32):
    return np.array(x[..., np.newaxis] == np.arange(size), dtype)