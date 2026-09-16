def make_header(self):
    cards = [fits.Card('TELESCOP', 'GLAST'), fits.Card('INSTRUME', 'LAT'),
        fits.Card(self._conv.coordsys, self._coordsys), fits.Card('PIXTYPE',
        'HEALPIX'), fits.Card('ORDERING', self.ordering), fits.Card('ORDER',
        self._order), fits.Card('NSIDE', self._nside), fits.Card('FIRSTPIX',
        0), fits.Card('LASTPIX', self._maxpix - 1), fits.Card('HPX_CONV',
        self._conv.convname)]
    if self._coordsys == 'CEL':
        cards.append(fits.Card('EQUINOX', 2000.0,
            'Equinox of RA & DEC specifications'))
    if self._region is not None:
        cards.append(fits.Card('HPX_REG', self._region))
        cards.append(fits.Card('INDXSCHM', 'PARTIAL'))
    elif self._ipix is not None:
        cards.append(fits.Card('INDXSCHM', 'EXPLICIT'))
    elif self._conv.convname in ['FGST_SRCMAP_SPARSE']:
        cards.append(fits.Card('INDXSCHM', 'SPARSE'))
    else:
        cards.append(fits.Card('INDXSCHM', 'IMPLICIT'))
    header = fits.Header(cards)
    return header