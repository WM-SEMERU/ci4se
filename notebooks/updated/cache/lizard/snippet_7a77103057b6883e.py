def easeInOutQuint(n):
    _checkRange(n)
    n = 2 * n
    if n < 1:
        return 0.5 * n ** 5
    else:
        n = n - 2
        return 0.5 * (n ** 5 + 2)