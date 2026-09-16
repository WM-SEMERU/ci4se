def train(self, ftrain):
    self.coeffs = 0 * self.coeffs
    upoints, wpoints = self.getQuadraturePointsAndWeights()
    try:
        fpoints = [ftrain(u) for u in upoints]
    except TypeError:
        fpoints = ftrain
    for ipoly in np.arange(self.N_poly):
        inds = tuple(self.index_polys[ipoly])
        coeff = 0.0
        for u, q, w in zip(upoints, fpoints, wpoints):
            coeff += eval_poly(u, inds, self.J_list) * q * np.prod(w)
        self.coeffs[inds] = coeff
    return None