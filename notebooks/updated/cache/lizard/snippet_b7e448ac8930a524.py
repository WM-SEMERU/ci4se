def calibrate_dates(chron, calib_curve, d_r, d_std, cutoff=0.0001,
    normal_distr=False, t_a=[3], t_b=[4]):
    n = len(chron.depth)
    calib_curve = np.array(calib_curve)
    t_a = np.array(t_a)
    t_b = np.array(t_b)
    assert t_b - 1 == t_a
    d_r = np.array(d_r)
    d_std = np.array(d_std)
    if len(t_a) == 1:
        t_a = np.repeat(t_a, n)
    if len(t_b) == 1:
        t_b = np.repeat(t_b, n)
    if len(d_r) == 1:
        d_r = np.repeat(d_r, n)
    if len(d_std) == 1:
        d_std = np.repeat(d_std, n)
    if len(calib_curve) == 1:
        calib_curve = np.repeat(calib_curve, n)
    calib_probs = []
    rcmean = chron.age - d_r
    w2 = chron.error ** 2 + d_std ** 2
    for i in range(n):
        age_realizations = d_cal(calib_curve[i], rcmean=rcmean[i], w2=w2[i],
            t_a=t_a[i], t_b=t_b[i], cutoff=cutoff, normal_distr=normal_distr)
        calib_probs.append(age_realizations)
    return np.array(chron.depth), calib_probs