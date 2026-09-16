def _compute_site_class_dummy_variables(cls, vs30):
    Sbc = np.zeros_like(vs30)
    Sc = np.zeros_like(vs30)
    Sd = np.zeros_like(vs30)
    Se = np.zeros_like(vs30)
    Sbc[vs30 > 760.0] = 1
    Sc[(vs30 > 360) & (vs30 <= 760)] = 1
    Sd[(vs30 >= 180) & (vs30 <= 360)] = 1
    Se[vs30 < 180] = 1
    return Sbc, Sc, Sd, Se