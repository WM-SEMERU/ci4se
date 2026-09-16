def append(self, term, type=None, value=None):
    term = self._normalize(term)
    type = self._normalize(type)
    self.setdefault(term, (odict(), odict()))[0].push((type, True))
    self.setdefault(type, (odict(), odict()))[1].push((term, True))
    self._values[term] = value