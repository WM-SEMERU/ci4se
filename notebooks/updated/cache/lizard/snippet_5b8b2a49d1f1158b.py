def gmst(utc_time):
    ut1 = jdays2000(utc_time) / 36525.0
    theta = 67310.54841 + ut1 * (876600 * 3600 + 8640184.812866 + ut1 * (
        0.093104 - ut1 * 6.2 * 1e-05))
    return np.deg2rad(theta / 240.0) % (2 * np.pi)