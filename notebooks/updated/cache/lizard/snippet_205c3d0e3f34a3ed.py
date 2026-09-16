def create_normal_logq(self, z):
    means, scale = self.get_means_and_scales()
    return ss.norm.logpdf(z, loc=means, scale=scale).sum()