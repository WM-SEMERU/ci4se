def _compute_soil_depth_term(self, C, imt, z1pt0, vs30):
    a21 = self._compute_a21_factor(C, imt, z1pt0, vs30)
    a22 = self._compute_a22_factor(imt)
    median_z1pt0 = self._compute_median_z1pt0(vs30)
    soil_depth_term = a21 * np.log((z1pt0 + self.CONSTS['c2']) / (
        median_z1pt0 + self.CONSTS['c2']))
    idx = z1pt0 >= 200
    soil_depth_term[idx] += a22 * np.log(z1pt0[idx] / 200)
    return soil_depth_term