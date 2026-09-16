def params(self):
    if self._params is None:
        self._params = list(filter(lambda attr: isinstance(attr, Param), [
            getattr(self, x) for x in dir(self) if x != 'params' and not
            isinstance(getattr(type(self), x, None), property)]))
    return self._params