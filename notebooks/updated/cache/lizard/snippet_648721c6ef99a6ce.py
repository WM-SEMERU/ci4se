def _get_a3_value(bbar, dbar, slip, beta, mmax):
    return dbar * (dbar - bbar) / bbar ** 2.0 * (slip / beta) * np.exp(-(
        dbar / 2.0) * mmax)