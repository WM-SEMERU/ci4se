def calc_mass_from_fit_and_conv_factor(A, Damping, ConvFactor):
    T0 = 300
    mFromA = 2 * Boltzmann * T0 / (pi * A) * ConvFactor ** 2 * Damping
    return mFromA