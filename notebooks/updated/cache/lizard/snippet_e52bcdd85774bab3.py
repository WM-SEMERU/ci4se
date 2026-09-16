def _load(self, scale=1.0):
    data = np.genfromtxt(self.requested_band_filename, unpack=True, names=[
        'wavenumber', 'response'], skip_header=4)
    wavelength = 1.0 / data['wavenumber'] * 10000.0
    response = data['response']
    detectors = {}
    detectors['det-1'] = {'wavelength': wavelength, 'response': response}
    self.rsr = detectors