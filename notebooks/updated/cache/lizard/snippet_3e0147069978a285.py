def _align_ast(self, a):
    try:
        if isinstance(a, BV):
            return self._align_bv(a)
        elif isinstance(a, Bool) and len(a.args) == 2 and a.args[1
            ].cardinality > a.args[0].cardinality:
            return self._reverse_comparison(a)
        else:
            return a
    except ClaripyBalancerError:
        return a