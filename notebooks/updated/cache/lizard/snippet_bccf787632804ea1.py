def merge_with(self, other, multiset_op, other_op=None):
    result = FeatureCollection()
    for ms_name in (set(self._counters()) | set(other._counters())):
        c1 = self.get(ms_name, None)
        c2 = other.get(ms_name, None)
        if c1 is None and c2 is not None:
            c1 = c2.__class__()
        if c2 is None and c1 is not None:
            c2 = c1.__class__()
        result[ms_name] = multiset_op(c1, c2)
    if other_op is not None:
        for o_name in (set(self._not_counters()) | set(other._not_counters())):
            v = other_op(self.get(o_name, None), other.get(o_name, None))
            if v is not None:
                result[o_name] = v
    return result