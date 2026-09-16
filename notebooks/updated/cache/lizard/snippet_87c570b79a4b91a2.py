def shift_to_coords(self, pix, fill_value=np.nan):
    pix_offset = self.get_offsets(pix)
    dpix = np.zeros(len(self.shape) - 1)
    for i in range(len(self.shape) - 1):
        x = self.rebin * (pix[i] - pix_offset[i + 1]) + (self.rebin - 1.0
            ) / 2.0
        dpix[i] = x - self._pix_ref[i]
    pos = [(pix_offset[i] + self.shape[i] // 2) for i in range(self.data.ndim)]
    s0, s1 = utils.overlap_slices(self.shape_out, self.shape, pos)
    k = np.zeros(self.data.shape)
    for i in range(k.shape[0]):
        k[i] = shift(self._data_spline[i], dpix, cval=np.nan, order=2,
            prefilter=False)
    for i in range(1, len(self.shape)):
        k = utils.sum_bins(k, i, self.rebin)
    k0 = np.ones(self.shape_out) * fill_value
    if k[s1].size == 0 or k0[s0].size == 0:
        return k0
    k0[s0] = k[s1]
    return k0