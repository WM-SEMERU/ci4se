def calculate_linear_attenuation_coefficient(atoms_per_cm3: np.float,
    sigma_b: np.array):
    miu_per_cm = 1e-24 * sigma_b * atoms_per_cm3
    return np.array(miu_per_cm)