def density_2d(self, x, y, rho0, gamma, center_x=0, center_y=0):
    x_ = x - center_x
    y_ = y - center_y
    r = np.sqrt(x_ ** 2 + y_ ** 2)
    sigma = np.sqrt(np.pi) * special.gamma(1.0 / 2 * (-1 + gamma)
        ) / special.gamma(gamma / 2.0) * r ** (1 - gamma) * rho0
    return sigma