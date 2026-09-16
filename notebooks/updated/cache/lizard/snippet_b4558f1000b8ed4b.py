def _polevl(x, coefs, N):
    ans = 0
    power = len(coefs) - 1
    for coef in coefs:
        try:
            ans += coef * x ** power
        except OverflowError:
            pass
        power -= 1
    return ans