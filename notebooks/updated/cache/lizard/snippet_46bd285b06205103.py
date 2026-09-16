def match(self, item):
    if self._position == len(self._matchers):
        raise RuntimeError('Matcher exhausted, no more matchers to use')
    matcher = self._matchers[self._position]
    if matcher(item):
        self._position += 1
    if self._position == len(self._matchers):
        return True
    return False