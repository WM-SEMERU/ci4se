def pca_eig(x):
    s, w = np.linalg.eigh(x.dot(x.T))
    return w, s