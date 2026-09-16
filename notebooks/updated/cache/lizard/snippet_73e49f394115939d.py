def addSpectrum(self, mzs, intensities, coords, userParams=[]):
    if self.mode != 'continuous' or self.first_mz is None:
        mzs = self.mz_compression.rounding(mzs)
    intensities = self.intensity_compression.rounding(intensities)
    if self.mode == 'continuous':
        if self.first_mz is None:
            self.first_mz = self._encode_and_write(mzs, self.mz_dtype, self
                .mz_compression)
        mz_data = self.first_mz
    elif self.mode == 'processed':
        mz_data = self._encode_and_write(mzs, self.mz_dtype, self.
            mz_compression)
    elif self.mode == 'auto':
        mz_data = self._get_previous_mz(mzs)
    else:
        raise TypeError('Unknown mode: %s' % self.mode)
    mz_offset, mz_len, mz_enc_len = mz_data
    int_offset, int_len, int_enc_len = self._encode_and_write(intensities,
        self.intensity_dtype, self.intensity_compression)
    mz_min = np.min(mzs)
    mz_max = np.max(mzs)
    ix_max = np.argmax(intensities)
    mz_base = mzs[ix_max]
    int_base = intensities[ix_max]
    int_tic = np.sum(intensities)
    s = _Spectrum(coords, mz_len, mz_offset, mz_enc_len, int_len,
        int_offset, int_enc_len, mz_min, mz_max, mz_base, int_base, int_tic,
        userParams)
    self.spectra.append(s)