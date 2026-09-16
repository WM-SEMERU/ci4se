def strip(self, chars=None):
    return self.__class__(self._str_strip('strip', chars), no_closing=chars and
        closing_code in chars)