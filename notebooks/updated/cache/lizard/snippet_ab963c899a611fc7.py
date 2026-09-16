def ansi_density(color, density_standard):
    sample = color.get_numpy_array()
    intermediate = sample * density_standard
    numerator = intermediate.sum()
    sum_of_standard_wavelengths = density_standard.sum()
    return -1.0 * log10(numerator / sum_of_standard_wavelengths)