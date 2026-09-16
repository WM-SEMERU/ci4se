def grav_pot(self, x, y, rho0, Rs, center_x=0, center_y=0):
    x_ = x - center_x
    y_ = y - center_y
    r = np.sqrt(x_ ** 2 + y_ ** 2)
    M = self.mass_tot(rho0, Rs)
    pot = M / (r + Rs)
    return pot