def _disc_kn(clearness_index, airmass, max_airmass=12):
    kt = clearness_index
    am = airmass
    am = np.minimum(am, max_airmass)
    kt2 = kt * kt
    kt3 = kt2 * kt
    bools = kt <= 0.6
    a = np.where(bools, 0.512 - 1.56 * kt + 2.286 * kt2 - 2.222 * kt3, -
        5.743 + 21.77 * kt - 27.49 * kt2 + 11.56 * kt3)
    b = np.where(bools, 0.37 + 0.962 * kt, 41.4 - 118.5 * kt + 66.05 * kt2 +
        31.9 * kt3)
    c = np.where(bools, -0.28 + 0.932 * kt - 2.048 * kt2, -47.01 + 184.2 *
        kt - 222.0 * kt2 + 73.81 * kt3)
    delta_kn = a + b * np.exp(c * am)
    Knc = (0.866 - 0.122 * am + 0.0121 * am ** 2 - 0.000653 * am ** 3 + 
        1.4e-05 * am ** 4)
    Kn = Knc - delta_kn
    return Kn, am