def _get_smr_coeffs(self, C, C_SITE, idx, n_sites, sa_rock):
    sreff = np.zeros(n_sites)
    sreffc = np.zeros(n_sites)
    f_sr = np.zeros(n_sites)
    for i in range(1, 5):
        sreff[idx[i]] += np.exp(sa_rock[idx[i]]) * self.IMF[i]
        sreffc[idx[i]] += C_SITE['Src1D{:g}'.format(i)] * self.IMF[i]
        f_sr[idx[i]] += C_SITE['fsr{:g}'.format(i)]
    return sreff, sreffc, f_sr