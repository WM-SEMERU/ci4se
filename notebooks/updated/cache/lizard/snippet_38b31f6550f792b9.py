def fourier_series(self, pars, x, order):
    sum = pars[0]
    for i in range(order):
        sum += pars[i * 2 + 1] * np.sin(2 * np.pi * (i + 1) * x) + pars[i *
            2 + 2] * np.cos(2 * np.pi * (i + 1) * x)
    return sum