def _get_satpos_cart(self):
    orbit_polynomial = self.prologue['SatelliteStatus']['Orbit'][
        'OrbitPolynomial']
    coef_idx = self._find_navigation_coefs()
    tstart = orbit_polynomial['StartTime'][0, coef_idx]
    tend = orbit_polynomial['EndTime'][0, coef_idx]
    time = self.prologue['ImageAcquisition']['PlannedAcquisitionTime'][
        'TrueRepeatCycleStart']
    time64 = np.datetime64(time).astype('int64')
    domain = [np.datetime64(tstart).astype('int64'), np.datetime64(tend).
        astype('int64')]
    x = chebyshev(coefs=orbit_polynomial['X'][coef_idx], time=time64,
        domain=domain)
    y = chebyshev(coefs=orbit_polynomial['Y'][coef_idx], time=time64,
        domain=domain)
    z = chebyshev(coefs=orbit_polynomial['Z'][coef_idx], time=time64,
        domain=domain)
    return x * 1000, y * 1000, z * 1000