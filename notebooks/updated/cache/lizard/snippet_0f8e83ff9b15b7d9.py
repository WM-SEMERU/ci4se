def get_layers(self, Psurf=1013.25, Ptop=0.01, **kwargs):
    Psurf = np.asarray(Psurf)
    output_ndims = Psurf.ndim + 1
    if output_ndims > 3:
        raise ValueError(
            '`Psurf` argument must be a float or an array with <= 2 dimensions (or None)'
            )
    SIGe = None
    SIGc = None
    ETAe = None
    ETAc = None
    if self.hybrid:
        try:
            Ap = broadcast_1d_array(self.Ap, output_ndims)
            Bp = broadcast_1d_array(self.Bp, output_ndims)
        except KeyError:
            raise ValueError(
                'Impossible to compute vertical levels, data is missing (Ap, Bp)'
                )
        Cp = 0.0
    else:
        try:
            Bp = SIGe = broadcast_1d_array(self.esig, output_ndims)
            SIGc = broadcast_1d_array(self.csig, output_ndims)
        except KeyError:
            raise ValueError(
                'Impossible to compute vertical levels, data is missing (esig, csig)'
                )
        Ap = Cp = Ptop
    Pe = Ap + Bp * (Psurf - Cp)
    Pc = 0.5 * (Pe[0:-1] + Pe[1:])
    if self.hybrid:
        ETAe = (Pe - Ptop) / (Psurf - Ptop)
        ETAc = (Pc - Ptop) / (Psurf - Ptop)
    else:
        SIGe = SIGe * np.ones_like(Psurf)
        SIGc = SIGc * np.ones_like(Psurf)
    Ze = prof_altitude(Pe, **kwargs)
    Zc = prof_altitude(Pc, **kwargs)
    all_vars = {'eta_edges': ETAe, 'eta_centers': ETAc, 'sigma_edges': SIGe,
        'sigma_centers': SIGc, 'pressure_edges': Pe, 'pressure_centers': Pc,
        'altitude_edges': Ze, 'altitude_centers': Zc}
    return all_vars