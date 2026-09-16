def arsh(self, num):
    if num < 0 or num > self.size:
        raise ValueError('expected 0 <= num <= {0.size}'.format(self))
    if num == 0:
        return self, self.__class__([], ftype=self.ftype)
    else:
        sign = self._items[-1]
        fs = self.__class__(self._items[num:] + [sign] * num, ftype=self.ftype)
        cout = self.__class__(self._items[:num], ftype=self.ftype)
        return fs, cout