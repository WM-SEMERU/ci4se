def fitPlaneLSQ(XYZ):
    [rows, cols] = XYZ.shape
    G = np.ones((rows, 3))
    G[:, (0)] = XYZ[:, (0)]
    G[:, (1)] = XYZ[:, (1)]
    Z = XYZ[:, (2)]
    coeff, resid, rank, s = np.linalg.lstsq(G, Z, rcond=None)
    return coeff