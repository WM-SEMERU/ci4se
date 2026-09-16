def moffat(self, x, p):
    y = (1.0 + (x - p[0]) ** 2 / p[1] ** 2) ** (-1.0 * p[2]) * p[3]
    return y