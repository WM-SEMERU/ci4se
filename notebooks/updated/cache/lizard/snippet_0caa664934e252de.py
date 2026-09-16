def pixscale(self):
    try:
        x, y = self['NAXIS1'] / 2.0, self['NAXIS2'] / 2.0
        p1 = SkyCoord(*(self.wcs.xy2sky(x, y) * units.degree))
        p2 = SkyCoord(*(self.wcs.xy2sky(x + 1, y + 1) * units.degree))
        return round(p1.separation(p2).to(units.arcsecond).value / math.
            sqrt(2), 3)
    except Exception as ex:
        logging.debug('Failed to compute PIXSCALE using WCS: {}'.format(ex))
    return float(self['PIXSCAL'])