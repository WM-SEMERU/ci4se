def Cmatrix(x, y, sx, sy, theta):
    C = np.vstack([elliptical_gaussian(x, y, 1, i, j, sx, sy, theta) for i,
        j in zip(x, y)])
    return C