def _xys(date):
    X, Y, s_xy2 = _xysxy2(date)
    dX, dY = date.eop.dx / 1000.0, date.eop.dy / 1000.0
    X = np.radians((X + dX) / 3600.0)
    Y = np.radians((Y + dY) / 3600.0)
    s = np.radians(s_xy2 / 3600.0) - X * Y / 2
    return X, Y, s