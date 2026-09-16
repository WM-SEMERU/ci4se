def check_thresholds(self):
    if not self._have_usage:
        self.find_usage()
    ret = {}
    for name, limit in self.limits.items():
        if limit.check_thresholds() is False:
            ret[name] = limit
    return ret