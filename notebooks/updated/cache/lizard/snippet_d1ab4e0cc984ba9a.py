def interpol_hist2d(h2d, oversamp_factor=10):
    from rootpy import ROOTError
    xlim = h2d.bins(axis=0)
    ylim = h2d.bins(axis=1)
    xn = h2d.nbins(0)
    yn = h2d.nbins(1)
    x = np.linspace(xlim[0], xlim[1], xn * oversamp_factor)
    y = np.linspace(ylim[0], ylim[1], yn * oversamp_factor)
    mat = np.zeros((xn, yn))
    for xi in range(xn):
        for yi in range(yn):
            try:
                mat[xi, yi] = h2d.interpolate(x[xi], y[yi])
            except ROOTError:
                continue
    return mat, x, y