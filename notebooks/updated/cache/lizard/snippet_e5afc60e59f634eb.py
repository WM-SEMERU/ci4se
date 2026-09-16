def findWhere(self, attrs=None):
    return self._wrap(self._clean.where(attrs, True))