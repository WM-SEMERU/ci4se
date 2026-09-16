def var_replace(self, text):
    result = text
    for var in self._vardict:
        result = result.replace('@{}'.format(var), self._vardict[var])
    return result