def get(self, stat_name=None):
    if stat_name is None:
        return self._thresholds
    if stat_name in self._thresholds:
        return self._thresholds[stat_name]
    else:
        return {}