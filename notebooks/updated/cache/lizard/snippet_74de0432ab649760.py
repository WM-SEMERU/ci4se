def zharkov_pel(v, temp, v0, e0, g, n, z, t_ref=300.0, three_r=3.0 *
    constants.R):
    v_mol = vol_uc2mol(v, z)
    x = v / v0

    def f(t):
        return three_r * n / 2.0 * e0 * np.power(x, g) * np.power(t, 2.0
            ) * g / v_mol * 1e-09
    return f(temp) - f(t_ref)