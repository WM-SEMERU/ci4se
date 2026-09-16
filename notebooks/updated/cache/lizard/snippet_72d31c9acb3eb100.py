def include_feature(self, name):
    if self.feature_is_included(name) == 0:
        descr = self.features[name].description
        raise DistutilsOptionError(descr +
            ' is required, but was excluded or is not available')
    self.features[name].include_in(self)
    self._set_feature(name, 1)