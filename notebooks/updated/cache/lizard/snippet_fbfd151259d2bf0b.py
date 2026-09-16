def _compute_mean(self, C, rup, dists, sites, imt):
    mean = self._compute_term_1_2(rup, C) + self._compute_term_3_4(dists, C
        ) + self._get_site_amplification(sites, imt, C)
    if imt.name == 'PGA':
        mean = np.exp(mean) / g / C['r_SA']
    else:
        W = 2.0 * np.pi / imt.period
        mean = np.exp(mean) * W / g / C['r_SA']
    return np.log(mean)