def mean_obliquity(jd_tdb):
    t = (jd_tdb - T0) / 36525.0
    epsilon = ((((-4.34e-08 * t - 5.76e-07) * t + 0.0020034) * t - 
        0.0001831) * t - 46.836769) * t + 84381.406
    return epsilon