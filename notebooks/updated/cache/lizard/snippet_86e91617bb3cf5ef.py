def mass_3d_lens(self, R, Rs, theta_Rs):
    rho0 = self._alpha2rho0(theta_Rs, Rs)
    m_3d = self.mass_3d(R, Rs, rho0)
    return m_3d