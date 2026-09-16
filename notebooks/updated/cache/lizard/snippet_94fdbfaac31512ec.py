def pan_by_pct(self, viewer, pct_x, pct_y, pad=0):
    pct_x = min(1.0, max(0.0, pct_x))
    pct_y = min(1.0, max(0.0, pct_y))
    limits = viewer.get_limits()
    tr = viewer.tform['data_to_scrollbar']
    mxwd, mxht = limits[1][:2]
    mxwd, mxht = mxwd + pad, mxht + pad
    mnwd, mnht = limits[0][:2]
    mnwd, mnht = mnwd - pad, mnht - pad
    arr = np.array([(mnwd, mnht), (mxwd, mnht), (mxwd, mxht), (mnwd, mxht)],
        dtype=np.float)
    x, y = tr.to_(arr).T
    rx1, rx2 = np.min(x), np.max(x)
    ry1, ry2 = np.min(y), np.max(y)
    crd_x = rx1 + pct_x * (rx2 - rx1)
    crd_y = ry1 + pct_y * (ry2 - ry1)
    pan_x, pan_y = tr.from_((crd_x, crd_y))
    self.logger.debug('crd=%f,%f pan=%f,%f' % (crd_x, crd_y, pan_x, pan_y))
    viewer.panset_xy(pan_x, pan_y)