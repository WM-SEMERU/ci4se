def Tran(m, x, rhol, rhog, mul, mug, sigma, D, roughness=0, L=1):
    r
    v_lo = m / rhol / (pi / 4 * D ** 2)
    Re_lo = Reynolds(V=v_lo, rho=rhol, mu=mul, D=D)
    fd_lo = friction_factor(Re=Re_lo, eD=roughness / D)
    dP_lo = fd_lo * L / D * (0.5 * rhol * v_lo ** 2)
    v_go = m / rhog / (pi / 4 * D ** 2)
    Re_go = Reynolds(V=v_go, rho=rhog, mu=mug, D=D)
    fd_go = friction_factor(Re=Re_go, eD=roughness / D)
    dP_go = fd_go * L / D * (0.5 * rhog * v_go ** 2)
    Gamma2 = dP_go / dP_lo
    Co = Confinement(D=D, rhol=rhol, rhog=rhog, sigma=sigma)
    phi_lo2 = 1 + (4.3 * Gamma2 - 1) * (Co * x ** 0.875 * (1 - x) ** 0.875 +
        x ** 1.75)
    return dP_lo * phi_lo2