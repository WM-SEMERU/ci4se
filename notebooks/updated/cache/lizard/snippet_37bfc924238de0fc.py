def copy(self):
    other = PackageFilter.__new__(PackageFilter)
    other._excludes = self._excludes.copy()
    other._includes = self._includes.copy()
    return other