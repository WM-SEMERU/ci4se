def dz_fltr_ma(dem, refdem, perc=None, rangelim=(0, 30), smooth=False):
    if smooth:
        refdem = gauss_fltr_astropy(refdem)
        dem = gauss_fltr_astropy(dem)
    dz = refdem - dem
    demmask = np.ma.getmaskarray(dem)
    if perc:
        dz_perc = malib.calcperc(dz, perc)
        print('Applying dz percentile filter (%s%%, %s%%): (%0.1f, %0.1f)' %
            (perc[0], perc[1], dz_perc[0], dz_perc[1]))
        perc_mask = ((dz < dz_perc[0]) | (dz > dz_perc[1])).filled(False)
        demmask = demmask | perc_mask
    if rangelim:
        range_mask = ((np.abs(dz) < rangelim[0]) | (np.abs(dz) > rangelim[1])
            ).filled(False)
        if False:
            cutoff = 150
            rangelim = 0, 80
            low = (refdem < cutoff).data
            range_mask[low] = ((np.abs(dz) < rangelim[0]) | (np.abs(dz) >
                rangelim[1])).filled(False)[low]
        demmask = demmask | range_mask
    out = np.ma.array(dem, mask=demmask, fill_value=dem.fill_value)
    return out