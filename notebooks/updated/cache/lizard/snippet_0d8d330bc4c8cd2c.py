def summary(self, name=None):
    warnings.warn(
        "'summary' is deprecated and will be removed in a future version.",
        FutureWarning, stacklevel=2)
    return self._summary(name)