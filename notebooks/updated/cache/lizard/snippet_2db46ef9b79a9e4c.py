def pot_ana(r, rho):
    I = 1.0
    sigma = 1.0 / rho
    phi = np.divide(I, 2.0 * np.pi * sigma * r)
    return phi