def bootstrap_noise(data, func, n=10000, std=1, symmetric=True):
    boot_dist = []
    arr = N.zeros(data.shape)
    for i in range(n):
        if symmetric:
            arr = N.random.randn(*data.shape) * std
        else:
            arr[:, (-1)] = N.random.randn(data.shape[0]) * std
        boot_dist.append(func(data + arr))
    return N.array(boot_dist)