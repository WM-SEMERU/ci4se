def _Tf(P, S):

    def f(T):
        T = float(T)
        pw = _Region1(T, P)
        gw = pw['h'] - T * pw['s']
        gih = _Ice(T, P)['g']
        ps = SeaWater._saline(T, P, S)
        return -ps['g'] + S * ps['gs'] - gw + gih
    Tf = fsolve(f, 300)[0]
    return Tf