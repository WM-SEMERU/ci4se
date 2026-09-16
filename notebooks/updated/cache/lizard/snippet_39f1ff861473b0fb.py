def kcore_bd(CIJ, k, peel=False):
    if peel:
        peelorder, peellevel = [], []
    iter = 0
    CIJkcore = CIJ.copy()
    while True:
        id, od, deg = degrees_dir(CIJkcore)
        ff, = np.where(np.logical_and(deg < k, deg > 0))
        if ff.size == 0:
            break
        iter += 1
        CIJkcore[(ff), :] = 0
        CIJkcore[:, (ff)] = 0
        if peel:
            peelorder.append(ff)
        if peel:
            peellevel.append(iter * np.ones((len(ff),)))
    kn = np.sum(deg > 0)
    if peel:
        return CIJkcore, kn, peelorder, peellevel
    else:
        return CIJkcore, kn