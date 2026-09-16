def castroData_from_ipix(self, ipix, colwise=False):
    if colwise:
        ipix = self._tsmap.ipix_swap_axes(ipix, colwise)
    norm_d = self._norm_vals[ipix]
    nll_d = self._nll_vals[ipix]
    return CastroData(norm_d, nll_d, self._refSpec, self._norm_type)