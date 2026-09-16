def tange_pth(v, temp, v0, gamma0, a, b, theta0, n, z, t_ref=300.0, three_r
    =3.0 * constants.R):
    v_mol = vol_uc2mol(v, z)
    gamma = tange_grun(v, v0, gamma0, a, b)
    theta = tange_debyetemp(v, v0, gamma0, a, b, theta0)
    xx = theta / temp
    debye = debye_E(xx)
    if t_ref == 0.0:
        debye0 = 0.0
    else:
        xx0 = theta / t_ref
        debye0 = debye_E(xx0)
    Eth0 = three_r * n * t_ref * debye0
    Eth = three_r * n * temp * debye
    delEth = Eth - Eth0
    p_th = gamma / v_mol * delEth * 1e-09
    return p_th