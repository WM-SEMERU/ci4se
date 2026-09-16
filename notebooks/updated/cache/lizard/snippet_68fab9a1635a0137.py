def cos_1(a=1):
    r

    def lhs(x):
        return np.exp(-a ** 2 * x ** 2)

    def rhs(b):
        return np.sqrt(np.pi) * np.exp(-b ** 2 / (4 * a ** 2)) / (2 * a)
    return Ghosh('cos', lhs, rhs)