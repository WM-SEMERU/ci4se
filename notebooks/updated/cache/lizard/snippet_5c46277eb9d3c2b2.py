def _forceRefreshMinMax(self):
    rangeMin, rangeMax = self.getTargetRange()
    maxOrder = np.log10(np.abs(max(rangeMax, rangeMin)))
    diffOrder = np.log10(np.abs(rangeMax - rangeMin))
    extraDigits = 2
    precisionF = np.clip(abs(maxOrder - diffOrder) + extraDigits, 
        extraDigits + 1, 25)
    precision = int(precisionF) if np.isfinite(precisionF) else extraDigits + 1
    self.rangeMinCti.precision = precision
    self.rangeMaxCti.precision = precision
    self.rangeMinCti.data, self.rangeMaxCti.data = rangeMin, rangeMax
    self.model.emitDataChanged(self.rangeMinCti)
    self.model.emitDataChanged(self.rangeMaxCti)