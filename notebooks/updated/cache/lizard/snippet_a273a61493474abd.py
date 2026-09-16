def tf_from_file(cls, path, delimiter=' '):
    data = np.loadtxt(path, delimiter=delimiter)
    freq = data[:, (0)]
    h = data[:, (1)] + 1.0j * data[:, (2)]
    return np.array([freq, h]).transpose()