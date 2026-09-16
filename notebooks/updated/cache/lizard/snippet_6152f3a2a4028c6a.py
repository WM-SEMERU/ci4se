def _print_DiracDelta(self, expr):
    return '{0}({1}, [{1} == 0 , {1} != 0], [{2}, 0])'.format(self.
        _module_format('numpy.piecewise'), self._print(expr.args[0]), self.
        _module_format('numpy.inf'))