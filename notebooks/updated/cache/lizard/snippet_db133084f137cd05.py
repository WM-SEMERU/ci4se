def _compute_site_scaling(self, vs30, mean):
    site_factor = np.ones(len(vs30), dtype=float)
    idx = vs30 <= 360.0
    site_factor[idx] = 1.4
    idx = vs30 > 760.0
    site_factor[idx] = 0.6
    return np.log(np.exp(mean) * site_factor)