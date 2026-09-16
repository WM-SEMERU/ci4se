def _compute_partial_derivative_site_amp(self, C, pga1100, vs30):
    delta_amp = np.zeros_like(vs30)
    vlin = C['VLIN']
    c = self.CONSTS['c']
    b = C['b']
    n = self.CONSTS['n']
    idx = vs30 < vlin
    delta_amp[idx] = -b * pga1100[idx] / (pga1100[idx] + c) + b * pga1100[idx
        ] / (pga1100[idx] + c * (vs30[idx] / vlin) ** n)
    return delta_amp