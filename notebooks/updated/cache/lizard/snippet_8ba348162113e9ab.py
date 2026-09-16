def bukin(self, x):
    s = 0
    for k in xrange((1 + len(x)) // 2):
        z = x[2 * k]
        y = x[min((2 * k + 1, len(x) - 1))]
        s += 100 * np.abs(y - 0.01 * z ** 2) ** 0.5 + 0.01 * np.abs(z + 10)
    return s