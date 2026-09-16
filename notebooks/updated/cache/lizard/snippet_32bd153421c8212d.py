def _convertPyval(self, oself, pyval):
    if pyval is None and not self.allowNone:
        raise TypeError('attribute [%s.%s = %s()] must not be None' % (self
            .classname, self.attrname, self.__class__.__name__))
    return self.infilter(pyval, oself, oself.store)