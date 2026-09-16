def footprint(self, nside=None):
    if nside is None:
        nside = self.nside_pixel
    elif nside < self.nside_catalog:
        raise Exception('Requested nside=%i is less than catalog_nside' % nside
            )
    elif nside > self.nside_pixel:
        raise Exception('Requested nside=%i is greater than pixel_nside' %
            nside)
    pix = np.arange(hp.nside2npix(nside), dtype=int)
    map = self.inFootprint(pix, nside)
    return map