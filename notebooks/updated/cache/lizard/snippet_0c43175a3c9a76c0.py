def brightness_prob(self, clip=True):
    thresh = 0.11
    bp = np.minimum(thresh, self.nir) / thresh
    if clip:
        bp[bp > 1] = 1
        bp[bp < 0] = 0
    return bp