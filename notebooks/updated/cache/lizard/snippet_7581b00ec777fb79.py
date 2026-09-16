def function(self, x, y, kappa_ext, ra_0=0, dec_0=0):
    theta, phi = param_util.cart2polar(x - ra_0, y - dec_0)
    f_ = 1.0 / 2 * kappa_ext * theta ** 2
    return f_