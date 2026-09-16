def trim(self, n_peaks):
    self.sortByIntensity()
    ims.spectrum_trim(self.ptr, n_peaks)