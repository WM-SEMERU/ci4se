def initbinflux(self):
    endpoints = binning.calculate_bin_edges(self.binwave)
    spwave = spectrum.MergeWaveSets(self.wave, endpoints)
    spwave = spectrum.MergeWaveSets(spwave, self.binwave)
    indices = np.searchsorted(spwave, endpoints)
    self._indices = indices[:-1]
    self._indices_last = indices[1:]
    flux = self(spwave)
    avflux = (flux[1:] + flux[:-1]) / 2.0
    self._deltaw = spwave[1:] - spwave[:-1]
    if utils_imported is True:
        self._binflux, self._intwave = pysynphot_utils.calcbinflux(len(self
            .binwave), self._indices, self._indices_last, avflux, self._deltaw)
    else:
        self._binflux = np.empty(shape=self.binwave.shape, dtype=np.float64)
        self._intwave = np.empty(shape=self.binwave.shape, dtype=np.float64)
        for i in range(len(self._indices)):
            first = self._indices[i]
            last = self._indices_last[i]
            self._binflux[i] = (avflux[first:last] * self._deltaw[first:last]
                ).sum() / self._deltaw[first:last].sum()
            self._intwave[i] = self._deltaw[first:last].sum()
    self._bin_edges = endpoints