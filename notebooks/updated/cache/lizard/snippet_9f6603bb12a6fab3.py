def print_profiles(self, w=0, cutoff=0, **print3opts):
    t = [(v, k) for k, v in _items(self._profs) if v.total > 0 or v.number > 1]
    if len(self._profs) - len(t) < 9:
        t = [(v, k) for k, v in _items(self._profs)]
    if t:
        s = ''
        if self._total:
            s = ' (% of grand total)'
            c = max(cutoff, self._cutoff)
            c = int(c * 0.01 * self._total)
        else:
            c = 0
        self._printf(
            '%s%*d profile%s:  total%s, average, and largest flat size%s:  largest object'
            , linesep, w, len(t), _plural(len(t)), s, self._incl, **print3opts)
        r = len(t)
        for v, k in _sorted(t, reverse=True):
            s = (
                'object%(plural)s:  %(total)s, %(avg)s, %(high)s:  %(obj)s%(lengstr)s'
                 % v.format(self._clip_, self._total))
            self._printf('%*d %s %s', w, v.number, self._prepr(k), s, **
                print3opts)
            r -= 1
            if r > 1 and v.total < c:
                c = max(cutoff, self._cutoff)
                self._printf('%+*d profiles below cutoff (%.0f%%)', w, r, c)
                break
        z = len(self._profs) - len(t)
        if z > 0:
            self._printf('%+*d %r object%s', w, z, 'zero', _plural(z), **
                print3opts)