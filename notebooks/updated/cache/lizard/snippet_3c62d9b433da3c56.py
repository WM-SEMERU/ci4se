def rhypo_to_rjb(rhypo, mag):
    epsilon = rhypo - (4.853 + 1.347e-06 * mag ** 8.163)
    rjb = np.zeros_like(rhypo)
    idx = epsilon >= 3.0
    rjb[idx] = np.sqrt(epsilon[idx] ** 2.0 - 9.0)
    rjb[rjb < 0.0] = 0.0
    return rjb