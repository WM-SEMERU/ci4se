def _delta_t_supconj_perpass(period, ecc, per0):
    ups_sc = np.pi / 2 - per0
    E_sc = 2 * np.arctan(np.sqrt((1 - ecc) / (1 + ecc)) * np.tan(ups_sc / 2))
    M_sc = E_sc - ecc * np.sin(E_sc)
    return period * (M_sc / 2.0 / np.pi)