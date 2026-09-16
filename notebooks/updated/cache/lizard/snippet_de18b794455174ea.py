def jackknife_indexes(data):
    base = np.arange(0, len(data))
    return (np.delete(base, i) for i in base)