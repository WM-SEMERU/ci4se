def xypix_to_ipix(self, xypix, colwise=False):
    return np.ravel_multi_index(xypix, self.npix, order='F' if colwise else
        'C', mode='raise')