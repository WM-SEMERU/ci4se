def offset_gaussian(data):
    nbins = 2 * int(np.ceil(np.sqrt(data.size)))
    mind, maxd = data.min(), data.max()
    drange = mind - (maxd - mind) / 2, maxd + (maxd - mind) / 2
    histo = np.histogram(data, nbins, density=True, range=drange)
    dx = abs(histo[1][1] - histo[1][2]) / 2
    hx = histo[1][1:] - dx
    hy = histo[0]
    gauss = lmfit.models.GaussianModel()
    pars = gauss.guess(hy, x=hx)
    out = gauss.fit(hy, pars, x=hx)
    return out.params['center']