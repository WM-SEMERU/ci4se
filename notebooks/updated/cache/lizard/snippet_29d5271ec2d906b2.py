def centroid(X):
    C = np.sum(X, axis=0) / len(X)
    return C