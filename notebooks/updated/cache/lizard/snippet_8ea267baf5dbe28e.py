def _dirint_from_dni_ktprime(dni, kt_prime, solar_zenith,
    use_delta_kt_prime, temp_dew):
    times = dni.index
    delta_kt_prime = _delta_kt_prime_dirint(kt_prime, use_delta_kt_prime, times
        )
    w = _temp_dew_dirint(temp_dew, times)
    dirint_coeffs = _dirint_coeffs(times, kt_prime, solar_zenith, w,
        delta_kt_prime)
    dni_dirint = dni * dirint_coeffs
    return dni_dirint