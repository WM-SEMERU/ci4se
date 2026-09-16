def rosen_nesterov(self, x, rho=100):
    f = 0.25 * (x[0] - 1) ** 2
    f += rho * sum((x[1:] - 2 * x[:-1] ** 2 + 1) ** 2)
    return f