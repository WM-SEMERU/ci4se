def Henry_H_at_T(T, H, Tderiv, T0=None, units=None, backend=None):
    be = get_backend(backend)
    if units is None:
        K = 1
    else:
        K = units.Kelvin
    if T0 is None:
        T0 = 298.15 * K
    return H * be.exp(Tderiv * (1 / T - 1 / T0))