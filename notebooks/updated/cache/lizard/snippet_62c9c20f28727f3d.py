def mass_3d(self, R, Rs, rho0):
    Rs = float(Rs)
    m_3d = 4.0 * np.pi * rho0 * Rs ** 3 * (np.log((Rs + R) / Rs) - R / (Rs + R)
        )
    return m_3d