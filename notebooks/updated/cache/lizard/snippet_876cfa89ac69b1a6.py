def _set_feature(self, name, status):
    setattr(self, self._feature_attrname(name), status)