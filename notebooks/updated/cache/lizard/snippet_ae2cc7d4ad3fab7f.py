def _Tb(P, S):

    def f(T):
        pw = _Region1(T, P)
        gw = pw['h'] - T * pw['s']
        pv = _Region2(T, P)
        gv = pv['h'] - T * pv['s']
        ps = SeaWater._saline(T, P, S)
        return -ps['g'] + S * ps['gs'] - gw + gv
    Tb = fsolve(f, 300)[0]
    return Tb