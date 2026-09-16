def _sizes(self, objs, sized=None):
    self.exclude_refs(*objs)
    s, t = {}, []
    for o in objs:
        i = id(o)
        if i in s:
            self._seen[i] += 1
            self._duplicate += 1
        else:
            s[i] = self._sizer(o, 0, sized)
        t.append(s[i])
    if sized:
        s = _sum([i.size for i in _values(s)])
    else:
        s = _sum(_values(s))
    self._total += s
    return s, tuple(t)