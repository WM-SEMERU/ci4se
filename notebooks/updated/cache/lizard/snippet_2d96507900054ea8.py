def _gcd(a=None, b=None, terms=None):
    if terms:
        return reduce(lambda a, b: _gcd(a, b), terms)
    else:
        while b:
            a, b = b, a % b
        return a