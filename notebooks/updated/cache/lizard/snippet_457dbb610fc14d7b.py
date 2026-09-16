def mk_getkw(kw, defaults, prefer_passed=False):

    def getkw(*ls):
        r = [(kw[l] if test(kw, l) else defaults[l]) for l in ls]
        if len(r) == 1:
            return r[0]
        return r

    def getkw_prefer_passed(*ls):
        r = [(kw[l] if l in kw else defaults[l]) for l in ls]
        if len(r) == 1:
            return r[0]
        return r
    return getkw if not prefer_passed else getkw_prefer_passed