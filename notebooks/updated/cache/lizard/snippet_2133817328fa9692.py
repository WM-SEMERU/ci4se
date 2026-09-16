def _outliers(self, x):
    outliers = self._tukey(x, threshold=1.5)
    return np.size(outliers)