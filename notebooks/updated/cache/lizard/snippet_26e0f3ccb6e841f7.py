def spline_matrix2d(x, y, px, py, mask=None):
    V = np.kron(spline_matrix(x, px), spline_matrix(y, py))
    lenV = len(V)
    if mask is not None:
        indices = np.nonzero(mask.T.flatten())
        if len(indices) > 1:
            indices = np.nonzero(mask.T.flatten())[1][0]
        newV = V.T[indices]
        V = newV.T
        V = V.reshape((V.shape[0], V.shape[1]))
    return V