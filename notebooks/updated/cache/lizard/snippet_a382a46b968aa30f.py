def chain_2(d2f_dg2, dg_dx, df_dg, d2g_dx2):
    if np.all(dg_dx == 1.0) and np.all(d2g_dx2 == 0):
        return d2f_dg2
    dg_dx_2 = np.clip(dg_dx, -np.inf, _lim_val_square) ** 2
    return d2f_dg2 * dg_dx_2 + df_dg * d2g_dx2