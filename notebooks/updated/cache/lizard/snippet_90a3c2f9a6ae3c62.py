def _unary_op(name, doc='unary operator'):

    def _(self):
        jc = getattr(self._jc, name)()
        return Column(jc)
    _.__doc__ = doc
    return _