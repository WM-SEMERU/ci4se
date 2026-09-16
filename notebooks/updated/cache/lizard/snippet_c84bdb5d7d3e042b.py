def _bin_op(name, doc='binary operator'):

    def _(self, other):
        jc = other._jc if isinstance(other, Column) else other
        njc = getattr(self._jc, name)(jc)
        return Column(njc)
    _.__doc__ = doc
    return _