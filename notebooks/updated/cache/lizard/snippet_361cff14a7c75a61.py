def mass_3d_lens(self, r, sigma0, Rs):
    rho0 = self.sigma2rho(sigma0, Rs)
    return self.mass_3d(r, rho0, Rs)