def get_incidence_matrix(self, fmt='coo'):
    r
    if fmt in self._im.keys():
        im = self._im[fmt]
    elif self._im.keys():
        im = self._am[list(self._im.keys())[0]]
        tofmt = getattr(im, 'to' + fmt)
        im = tofmt()
        self._im[fmt] = im
    else:
        im = self.create_incidence_matrix(weights=self.Ts, fmt=fmt)
        self._im[fmt] = im
    return im