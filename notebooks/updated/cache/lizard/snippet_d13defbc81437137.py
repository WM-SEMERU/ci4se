def gammatone_erb_constants(n):
    tnt = 2 * n - 2
    return factorial(n - 1) ** 2 / (pi * factorial(tnt) * 2 ** -tnt), 2 * (
        2 ** (1.0 / n) - 1) ** 0.5