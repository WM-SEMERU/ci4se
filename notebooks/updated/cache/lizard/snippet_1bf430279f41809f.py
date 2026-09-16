def _tilt(omega, b, psi):
    return np.cosh(psi / 2.0) ** b * np.exp(-psi ** 2 / 2.0 * omega)