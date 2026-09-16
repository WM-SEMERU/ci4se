def get_xy_ma(bma, gt, stride=1, origmask=True, newmask=None):
    pX = np.arange(0, bma.shape[1], stride)
    pY = np.arange(0, bma.shape[0], stride)
    psamp = np.meshgrid(pX, pY)
    mX, mY = pixelToMap(psamp[0], psamp[1], gt)
    mask = None
    if origmask:
        mask = np.ma.getmaskarray(bma)[::stride]
    if newmask is not None:
        mask = newmask[::stride]
    mX = np.ma.array(mX, mask=mask, fill_value=0)
    mY = np.ma.array(mY, mask=mask, fill_value=0)
    return mX, mY