def _compute_hanging_wall_effect(self, C, rjb, rrup, dip, mag):
    hw = np.zeros_like(rjb)
    if dip <= 70.0:
        hw = (5.0 - rjb) / 5.0
    f_m = 1 if mag > 6.5 else mag - 5.5
    f_rrup = C['c15'] + np.zeros_like(rrup)
    idx = rrup < 8
    f_rrup[idx] *= rrup[idx] / 8
    f_hw = hw * f_m * f_rrup
    return f_hw