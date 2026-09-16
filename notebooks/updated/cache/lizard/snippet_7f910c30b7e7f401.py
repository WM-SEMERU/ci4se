def _func(self, volume, params):
    e0, b0, b1, v0 = tuple(params)
    return e0 + 9.0 / 8.0 * b0 * v0 * ((v0 / volume) ** (2.0 / 3.0) - 1.0
        ) ** 2 + 9.0 / 16.0 * b0 * v0 * (b1 - 4.0) * ((v0 / volume) ** (2.0 /
        3.0) - 1.0) ** 3