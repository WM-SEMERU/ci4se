def logpdf_link(self, link_f, y, Y_metadata=None):
    return -link_f + y * np.log(link_f) - special.gammaln(y + 1)