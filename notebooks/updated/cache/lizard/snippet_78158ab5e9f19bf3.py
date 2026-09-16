def _get_SRF_tau(self, imt_per):
    if imt_per < 1:
        srf = 0.87
    elif 1 <= imt_per < 5:
        srf = self._interp_function(0.58, 0.87, 5, 1, imt_per)
    elif 5 <= imt_per <= 10:
        srf = 0.58
    else:
        srf = 1
    return srf