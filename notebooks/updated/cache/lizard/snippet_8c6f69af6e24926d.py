def css_class(self, cell):
    if isinstance(self._css_class, basestring):
        return self._css_class
    else:
        return self._css_class(cell)