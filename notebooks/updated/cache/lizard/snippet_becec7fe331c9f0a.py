def _compute_geometrical_spreading_term(self, C, rrup):
    f2 = np.ones_like(rrup)
    idx1 = np.nonzero(rrup <= 70.0)
    idx2 = np.nonzero((rrup > 70.0) & (rrup <= 130.0))
    idx3 = np.nonzero(rrup > 130.0)
    f2[idx1] = C['c9'] * np.log(rrup[idx1] + 4.5)
    f2[idx2] = C['c10'] * np.log(rrup[idx2] / 70.0) + C['c9'] * np.log(rrup
        [idx2] + 4.5)
    f2[idx3] = C['c11'] * np.log(rrup[idx3] / 130.0) + C['c10'] * np.log(
        rrup[idx3] / 70.0) + C['c9'] * np.log(rrup[idx3] + 4.5)
    return f2