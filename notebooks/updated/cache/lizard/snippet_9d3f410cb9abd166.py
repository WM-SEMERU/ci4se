def double_sphere(cdata, sym):
    nrows = cdata.shape[0]
    ncols = cdata.shape[1]
    ddata = np.zeros([nrows, ncols], dtype=np.complex128)
    for n in xrange(0, nrows):
        for m in xrange(0, ncols):
            s = sym * cdata[np.mod(nrows - n, nrows), np.mod(int(np.floor(
                ncols / 2)) + m, ncols)]
            t = cdata[n, m]
            if s * t == 0:
                ddata[n, m] = s + t
            else:
                ddata[n, m] = (s + t) / 2
    return ddata