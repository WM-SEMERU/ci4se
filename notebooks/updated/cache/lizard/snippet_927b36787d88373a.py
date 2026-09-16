def find_rotation_scale(im0, im1, isccs=False):
    im0 = np.asarray(im0, dtype=np.float32)
    im1 = np.asarray(im1, dtype=np.float32)
    truesize = None
    if isccs:
        truesize = im0.shape
        im0 = centered_mag_sq_ccs(im0)
        im1 = centered_mag_sq_ccs(im1)
    lp1, log_base = polar_fft(im1, logpolar=True, isshiftdft=isccs,
        logoutput=True, truesize=truesize)
    lp0, log_base = polar_fft(im0, logpolar=True, isshiftdft=isccs,
        logoutput=True, truesize=truesize, nangle=lp1.shape[0], radiimax=
        lp1.shape[1])
    angle, scale = find_shift_dft(lp0, lp1)
    angle *= np.pi / lp1.shape[0]
    scale = log_base ** scale
    return angle, scale