def expected_distorted_boundaries(islitlet, csu_bar_slit_center, borderlist,
    params, parmodel, numpts, deg, debugplot=0):
    c2, c4, ff, slit_gap, slit_height, theta0, x0, y0, y_baseline = (
        return_params(islitlet, csu_bar_slit_center, params, parmodel))
    xp = np.linspace(1, EMIR_NAXIS1, numpts)
    slit_dist = slit_height * 10 + slit_gap
    ybottom = y_baseline * 100 + (islitlet - 1) * slit_dist
    ytop = ybottom + slit_height * 10
    list_spectrails = []
    for borderval in borderlist:
        yvalue = ybottom + borderval * (ytop - ybottom)
        yp_value = np.ones(numpts) * yvalue
        xdist, ydist = exvp(xp, yp_value, x0=x0, y0=y0, c2=c2, c4=c4,
            theta0=theta0, ff=ff)
        spectrail = SpectrumTrail()
        spectrail.fit(x=xdist, y=ydist, deg=deg, debugplot=debugplot)
        list_spectrails.append(spectrail)
    return list_spectrails