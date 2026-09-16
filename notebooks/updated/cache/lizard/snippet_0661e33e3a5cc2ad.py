def median_fltr_skimage(dem, radius=3, erode=1, origmask=False):
    dem = malib.checkma(dem)
    dem = dem.astype(np.float64)
    if erode > 0:
        print('Eroding islands smaller than %s pixels' % (erode * 2))
        dem = malib.mask_islands(dem, iterations=erode)
    print('Applying median filter with radius %s' % radius)
    import skimage.filter
    dem_filt_med = skimage.filter.median_filter(dem, radius, mask=~dem.mask)
    ndv = np.min(dem_filt_med)
    out = np.ma.masked_less_equal(dem_filt_med, ndv)
    out.set_fill_value(dem.fill_value)
    if origmask:
        print('Applying original mask')
        maskfill = malib.maskfill(dem)
        out = np.ma.array(out, mask=maskfill, fill_value=dem.fill_value)
    return out