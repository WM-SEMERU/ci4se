def function(self, x, y, amp, R_sersic, n_sersic, e1, e2, center_x=0,
    center_y=0):
    R_sersic = np.maximum(0, R_sersic)
    phi_G, q = param_util.ellipticity2phi_q(e1, e2)
    x_shift = x - center_x
    y_shift = y - center_y
    cos_phi = np.cos(phi_G)
    sin_phi = np.sin(phi_G)
    xt1 = cos_phi * x_shift + sin_phi * y_shift
    xt2 = -sin_phi * x_shift + cos_phi * y_shift
    xt2difq2 = xt2 / (q * q)
    R_ = np.sqrt(xt1 * xt1 + xt2 * xt2difq2)
    if isinstance(R_, int) or isinstance(R_, float):
        R_ = max(self._smoothing, R_)
    else:
        R_[R_ < self._smoothing] = self._smoothing
    k, bn = self.k_bn(n_sersic, R_sersic)
    R_frac = R_ / R_sersic
    R_frac = R_frac.astype(np.float32)
    if isinstance(R_, int) or isinstance(R_, float):
        if R_frac > 100:
            result = 0
        else:
            exponent = -bn * (R_frac ** (1.0 / n_sersic) - 1.0)
            result = amp * np.exp(exponent)
    else:
        R_frac_real = R_frac[R_frac <= 100]
        exponent = -bn * (R_frac_real ** (1.0 / n_sersic) - 1.0)
        result = np.zeros_like(R_)
        result[R_frac <= 100] = amp * np.exp(exponent)
    return np.nan_to_num(result)