def d2logpdf_dlink2(self, inv_link_f, y, Y_metadata=None):
    e = y - inv_link_f
    hess = (self.v + 1) * (e ** 2 - self.v * self.sigma2) / (self.sigma2 *
        self.v + e ** 2) ** 2
    return hess