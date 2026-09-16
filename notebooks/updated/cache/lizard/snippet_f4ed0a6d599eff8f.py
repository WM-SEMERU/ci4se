def _gamma_difference_hrf(tr, oversampling=50, time_length=32.0, onset=0.0,
    delay=6, undershoot=16.0, dispersion=1.0, u_dispersion=1.0, ratio=0.167):
    from scipy.stats import gamma
    dt = tr / oversampling
    time_stamps = np.linspace(0, time_length, np.rint(float(time_length) /
        dt).astype(np.int))
    time_stamps -= onset
    hrf = gamma.pdf(time_stamps, delay / dispersion, dt / dispersion
        ) - ratio * gamma.pdf(time_stamps, undershoot / u_dispersion, dt /
        u_dispersion)
    hrf /= hrf.sum()
    return hrf