def d2logpdf_dlink2_dvar(self, inv_link_f, y, Y_metadata=None):
    e = y - inv_link_f
    d2logpdf_dlink2_dvar = self.v * (self.v + 1) * (self.sigma2 * self.v - 
        3 * e ** 2) / (self.sigma2 * self.v + e ** 2) ** 3
    return d2logpdf_dlink2_dvar