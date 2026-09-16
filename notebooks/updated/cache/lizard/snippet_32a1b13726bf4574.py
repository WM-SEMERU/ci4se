def generate_moffat_profile(seeing_fwhm, alpha):
    scale = 2 * math.sqrt(2 ** (1.0 / alpha) - 1)
    gamma = seeing_fwhm / scale
    amplitude = 1.0 / math.pi * (alpha - 1) / gamma ** 2
    seeing_model = Moffat2D(amplitude=amplitude, x_mean=0.0, y_mean=0.0,
        gamma=gamma, alpha=alpha)
    return seeing_model