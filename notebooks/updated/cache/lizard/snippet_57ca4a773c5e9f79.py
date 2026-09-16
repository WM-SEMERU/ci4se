def _intersection_with_dsis(self, dsis):
    new_si_set = set()
    for si in dsis._si_set:
        r = self._intersection_with_si(si)
        if isinstance(r, StridedInterval):
            if not r.is_empty:
                new_si_set.add(r)
        else:
            new_si_set |= r._si_set
    if len(new_si_set):
        ret = DiscreteStridedIntervalSet(bits=self.bits, si_set=new_si_set)
        return ret.normalize()
    else:
        return StridedInterval.empty(self.bits)