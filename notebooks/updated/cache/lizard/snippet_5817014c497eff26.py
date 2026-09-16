def factorial_recur(n, mod=None):
    if not (isinstance(n, int) and n >= 0):
        raise ValueError("'n' must be a non-negative integer.")
    if mod is not None and not (isinstance(mod, int) and mod > 0):
        raise ValueError("'mod' must be a positive integer")
    if n == 0:
        return 1
    result = n * factorial(n - 1, mod)
    if mod:
        result %= mod
    return result