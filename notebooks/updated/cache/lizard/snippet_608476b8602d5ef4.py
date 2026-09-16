def ellipticities(I_xy, x, y):
    Q_xx, Q_xy, Q_yy, bkg = moments(I_xy, x, y)
    norm = Q_xx + Q_yy + 2 * np.sqrt(Q_xx * Q_yy - Q_xy ** 2)
    e1 = (Q_xx - Q_yy) / norm
    e2 = 2 * Q_xy / norm
    return e1 / (1 + bkg), e2 / (1 + bkg)