def log_normalize(data):
    if sp.issparse(data):
        data = data.copy()
        data.data = np.log2(data.data + 1)
        return data
    return np.log2(data.astype(np.float64) + 1)