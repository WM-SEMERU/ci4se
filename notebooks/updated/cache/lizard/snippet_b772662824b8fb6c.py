def isothermal_gas(rho, fd, P1=None, P2=None, L=None, D=None, m=None):
    ans = wrapped_isothermal_gas(rho, fd, P1, P2, L, D, m)
    if m is None and None not in [P1, P2, L, D]:
        return ans * u.kg / u.s
    elif L is None and None not in [P1, P2, D, m]:
        return ans * u.m
    elif P1 is None and None not in [L, P2, D, m]:
        return ans * u.Pa
    elif P2 is None and None not in [L, P1, D, m]:
        return ans * u.Pa
    elif D is None and None not in [P2, P1, L, m]:
        return ans * u.m