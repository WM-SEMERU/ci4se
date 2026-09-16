def regex(self, regex=None):
    if regex is None:
        return self._regex
    if self._type != 'string':
        sys.stderr.write('can not set __regex__ for %s' % self._type)
        return
    if not isinstance(regex, (basestring, _REGEX_TYPE)):
        raise ValueError('__regex__')
    self._regex = regex