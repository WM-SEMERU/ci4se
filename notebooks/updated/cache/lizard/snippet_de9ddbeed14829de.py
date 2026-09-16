def Planck_wavelength(l, T):
    u = hPlanck * c_light / l / kBoltzmann / T
    return (2 * kBoltzmann ** 5 * T ** 5 / hPlanck ** 4 / c_light ** 3 * u **
        5 / (exp(u) - 1))