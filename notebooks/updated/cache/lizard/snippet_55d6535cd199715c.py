def mapToPixel(mX, mY, geoTransform):
    mX = np.asarray(mX)
    mY = np.asarray(mY)
    if geoTransform[2] + geoTransform[4] == 0:
        pX = (mX - geoTransform[0]) / geoTransform[1] - 0.5
        pY = (mY - geoTransform[3]) / geoTransform[5] - 0.5
    else:
        pX, pY = applyGeoTransform(mX, mY, invertGeoTransform(geoTransform))
    return pX, pY