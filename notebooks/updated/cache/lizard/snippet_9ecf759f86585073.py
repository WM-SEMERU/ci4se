def max(self):
    res = self._qexec('max(%s)' % self._name)
    if len(res) > 0:
        self._max = res[0][0]
    return self._max