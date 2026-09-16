def warn(self, key):
    return not self.quiet and not self.warn_none and (self.warn_all or
        getattr(self, 'warn_%s' % key))