def haeberlen_values(self):
    pas = self.principal_axis_system
    sigma_iso = pas.trace() / 3
    sigmas = np.diag(pas)
    sigmas = sorted(sigmas, key=lambda x: np.abs(x - sigma_iso))
    sigma_yy, sigma_xx, sigma_zz = sigmas
    delta_sigma = sigma_zz - 0.5 * (sigma_xx + sigma_yy)
    zeta = sigma_zz - sigma_iso
    eta = (sigma_yy - sigma_xx) / zeta
    return self.HaeberlenNotation(sigma_iso, delta_sigma, zeta, eta)