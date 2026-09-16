def fft(fEM, time, freq, ftarg):
    r
    dfreq, nfreq, ntot, pts_per_dec = ftarg
    if pts_per_dec:
        sfEMr = iuSpline(np.log(freq), fEM.real)
        sfEMi = iuSpline(np.log(freq), fEM.imag)
        freq = np.arange(1, nfreq + 1) * dfreq
        fEM = sfEMr(np.log(freq)) + 1.0j * sfEMi(np.log(freq))
    fEM = np.pad(fEM, (0, ntot - nfreq), 'linear_ramp')
    ifftEM = fftpack.ifft(np.r_[fEM[1:], 0, fEM[::-1].conj()]).real
    stEM = 2 * ntot * fftpack.fftshift(ifftEM * dfreq, 0)
    dt = 1 / (2 * ntot * dfreq)
    ifEM = iuSpline(np.linspace(-ntot, ntot - 1, 2 * ntot) * dt, stEM)
    tEM = ifEM(time) / 2 * np.pi
    return tEM, True