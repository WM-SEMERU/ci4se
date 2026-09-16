def splinefit2d(x, y, z, px, py, mask=None):
    if mask is None:
        V = np.array(spline_matrix2d(x, y, px, py))
        a = np.array(z.T.flatten())
        pz = np.linalg.lstsq(V.T, a.T)[0].T
    else:
        V = np.array(spline_matrix2d(x, y, px, py, mask))
        indices = np.nonzero(np.array(mask).T.flatten())
        if len(indices[0]) == 0:
            pz = np.zeros((len(py), len(px)))
        else:
            a = np.array(z.T.flatten()[indices[0]])
            pz = np.linalg.lstsq(V.T, a.T)[0].T
    pz = pz.reshape((len(py), len(px)))
    return pz.transpose()