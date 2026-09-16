def create_periodic(mu_err=0.0, sigma_err=1.0, seed=None, **kwargs):
    random = np.random.RandomState(seed)
    size = kwargs.get('size', DEFAULT_SIZE)
    times, mags, errors = [], [], []
    for b in kwargs.get('bands', BANDS):
        time = 100 * random.rand(size)
        error = random.normal(size=size, loc=mu_err, scale=sigma_err)
        mag = np.sin(2 * np.pi * time) + error * random.randn(size)
        times.append(time)
        errors.append(error)
        mags.append(mag)
    times, mags, errors = iter(times), iter(mags), iter(errors)
    return create_random(magf=lambda **k: next(mags), magf_params={}, errf=
        lambda **k: next(errors), errf_params={}, timef=lambda **k: next(
        times), timef_params={}, **kwargs)