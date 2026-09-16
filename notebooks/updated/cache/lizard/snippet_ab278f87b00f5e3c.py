def compute_log_scales(lmin, lmax, Nscales, t1=1, t2=2):
    r
    scale_min = t1 / lmax
    scale_max = t2 / lmin
    return np.exp(np.linspace(np.log(scale_max), np.log(scale_min), Nscales))