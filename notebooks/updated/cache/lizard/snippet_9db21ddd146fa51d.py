def format(self):
    if self.dynamic_version_of is not None:
        return self.dynamic_version_of.format
    if not self._format:
        self._format = '%s_%%s' % self.name
    return self._format