def _get_regional_term(self, C, imt, vs30, rrup):
    f3 = interpolate.interp1d([150, 250, 350, 450, 600, 850, 1150, 2000], [
        C['a36'], C['a37'], C['a38'], C['a39'], C['a40'], C['a41'], C['a42'
        ], C['a42']], kind='linear')
    return f3(vs30) + C['a29'] * rrup