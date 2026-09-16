def get_xy_grids(ds, stride=1, getval=False):
    gt = ds.GetGeoTransform()
    pX = np.arange(0, ds.RasterXSize, stride)
    pY = np.arange(0, ds.RasterYSize, stride)
    psamp = np.meshgrid(pX, pY)
    mX, mY = pixelToMap(psamp[0], psamp[1], gt)
    return mX, mY