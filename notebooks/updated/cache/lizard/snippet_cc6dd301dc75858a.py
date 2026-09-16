def glover_dispersion_derivative(tr, oversampling=50, time_length=32.0,
    onset=0.0):
    dd = 0.01
    dhrf = 1.0 / dd * (-_gamma_difference_hrf(tr, oversampling, time_length,
        onset, delay=6, undershoot=12.0, dispersion=0.9 + dd, ratio=0.35) +
        _gamma_difference_hrf(tr, oversampling, time_length, onset, delay=6,
        undershoot=12.0, dispersion=0.9, ratio=0.35))
    return dhrf