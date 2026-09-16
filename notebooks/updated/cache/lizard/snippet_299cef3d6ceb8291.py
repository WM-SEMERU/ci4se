def _fourier(self):
    freq_bin_upper = 2000
    freq_bin_lower = 40
    fs = self._metadata['fs']
    Y_transformed = {}
    for key in self.Y_dict.keys():
        fs = self._metadata['fs']
        Y_transformed[key] = 1.0 / fs * np.fft.fft(self.Y_dict[key])[
            freq_bin_lower:freq_bin_upper]
    self.Y_transformed = Y_transformed
    self._metadata['dF'] = 1.0 / self._metadata['T']
    self.psd = load_psd()[freq_bin_lower:freq_bin_upper]
    dF = self._metadata['dF']
    self.sigma = convert_psd_to_sigma(self.psd, dF)