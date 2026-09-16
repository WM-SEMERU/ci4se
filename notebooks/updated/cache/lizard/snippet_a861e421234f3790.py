def easeOutBack(n, s=1.70158):
    _checkRange(n)
    n = n - 1
    return n * n * ((s + 1) * n + s) + 1