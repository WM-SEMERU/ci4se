def _dirint_coeffs(times, kt_prime, solar_zenith, w, delta_kt_prime):
    kt_prime_bin, zenith_bin, w_bin, delta_kt_prime_bin = _dirint_bins(times,
        kt_prime, solar_zenith, w, delta_kt_prime)
    coeffs = _get_dirint_coeffs()
    dirint_coeffs = coeffs[kt_prime_bin - 1, zenith_bin - 1, 
        delta_kt_prime_bin - 1, w_bin - 1]
    dirint_coeffs = np.where((kt_prime_bin == 0) | (zenith_bin == 0) | (
        w_bin == 0) | (delta_kt_prime_bin == 0), np.nan, dirint_coeffs)
    return dirint_coeffs