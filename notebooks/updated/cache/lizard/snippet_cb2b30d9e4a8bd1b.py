def _compute_slab_correction_term(self, C, rrup):
    slab_term = C['SSL'] * np.log(rrup)
    return slab_term