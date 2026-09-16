def earth_tilt(t):
    dp, de = t._nutation_angles
    c_terms = equation_of_the_equinoxes_complimentary_terms(t.tt) / ASEC2RAD
    d_psi = dp * 1e-07 + t.psi_correction
    d_eps = de * 1e-07 + t.eps_correction
    mean_ob = mean_obliquity(t.tdb)
    true_ob = mean_ob + d_eps
    mean_ob /= 3600.0
    true_ob /= 3600.0
    eq_eq = d_psi * cos(mean_ob * DEG2RAD) + c_terms
    eq_eq /= 15.0
    return mean_ob, true_ob, eq_eq, d_psi, d_eps