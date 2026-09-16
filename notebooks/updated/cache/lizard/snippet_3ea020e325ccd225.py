def make_r_gaussmix(data, K_g=15, critical_r=2.0, indices=None, approx=False):
    return _mkgauss(*_make_r_patches(data, K_g, critical_r, indices, approx))