def verify_checksum(self):
    res = self._FITS.verify_checksum(self._ext + 1)
    if res['dataok'] != 1:
        raise ValueError('data checksum failed')
    if res['hduok'] != 1:
        raise ValueError('hdu checksum failed')