def breadthdist(CIJ):
    n = len(CIJ)
    D = np.zeros((n, n))
    for i in range(n):
        D[(i), :], _ = breadth(CIJ, i)
    D[D == 0] = np.inf
    R = D != np.inf
    return R, D