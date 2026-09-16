def calc_fwhm(img, region, fexpand=3, axis=0):
    xpregion = expand_region(region, fexpand, fexpand)
    cslit = img[xpregion]
    pslit = cslit.mean(axis=axis)
    x2 = len(pslit)
    y1, y2 = pslit[0], pslit[-1]
    mslope = (y2 - y1) / x2
    backstim = mslope * numpy.arange(x2) + y1
    qslit = pslit - backstim
    pidx = numpy.argmax(qslit)
    peak, fwhm = fmod.compute_fwhm_1d_simple(qslit, pidx)
    return fwhm