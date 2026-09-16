def _alpha2rho0(self, theta_Rs, Rs):
    rho0 = theta_Rs / (4.0 * Rs ** 2 * (1.0 + np.log(1.0 / 2.0)))
    return rho0