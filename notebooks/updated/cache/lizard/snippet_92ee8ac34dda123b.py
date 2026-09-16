def _delta_sigma(**cosmo):
    M8_cosmo = cp.perturbation.radius_to_mass(8, **cosmo)
    perturbed_A = 0.796 / cosmo['sigma_8'] * (M8_cosmo / 250000000000000.0
        ) ** ((cosmo['n'] - 0.963) / 6)
    return perturbed_A