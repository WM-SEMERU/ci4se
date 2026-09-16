def define_simplification(omega_level, xi, Nl):
    try:
        Ne = len(omega_level)
    except:
        Ne = omega_level.shape[0]
    om = omega_level[0]
    iu = 0
    Neu = 1
    omega_levelu = [om]
    d = {}
    di = {(0): 0}
    for i in range(Ne):
        if omega_level[i] != om:
            iu += 1
            om = omega_level[i]
            Neu += 1
            omega_levelu += [om]
            di.update({iu: i})
        d.update({i: iu})

    def u(i):
        return d[i]

    def invu(iu):
        return di[iu]
    Neu = len(omega_levelu)
    xiu = np.array([[[xi[l, invu(i), invu(j)] for j in range(Neu)] for i in
        range(Neu)] for l in range(Nl)])
    return u, invu, omega_levelu, Neu, xiu