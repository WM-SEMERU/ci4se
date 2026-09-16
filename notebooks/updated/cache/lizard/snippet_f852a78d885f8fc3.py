def _load(self, scale=1.0):
    LOG.debug('File: %s', str(self.requested_band_filename))
    ncf = Dataset(self.requested_band_filename, 'r')
    wvl = ncf.variables['wavelength'][:] * scale
    resp = ncf.variables['response'][:]
    self.rsr = {'wavelength': wvl, 'response': resp}