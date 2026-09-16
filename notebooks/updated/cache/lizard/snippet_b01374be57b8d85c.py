def get_rate_osr_normal_transform(self, threshold_moment, id0):
    e1h_ridge = np.zeros(np.sum(id0), dtype=float)
    e2h_ridge = self.strain.data['e1h'][id0] + self.strain.data['e2h'][id0]
    err_ridge = -(e1h_ridge + e2h_ridge)
    calculated_rate_ridge = self.continuum_seismicity(threshold_moment,
        e1h_ridge, e2h_ridge, err_ridge, self.regionalisation['OSRnor'])
    e1h_trans = self.strain.data['e1h'][id0]
    e2h_trans = -e1h_trans
    err_trans = np.zeros(np.sum(id0), dtype=float)
    calculated_rate_transform = self.continuum_seismicity(threshold_moment,
        e1h_trans, e2h_trans, err_trans, self.regionalisation['OTFmed'])
    return self.regionalisation['OSRnor']['adjustment_factor'] * (
        calculated_rate_ridge + calculated_rate_transform)