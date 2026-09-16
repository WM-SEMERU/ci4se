def k_s(X):
    xbar, sigma = pmag.gausspars(X)
    d, f = 0, 0.0
    for i in range(1, len(X) + 1):
        b = old_div(float(i), float(len(X)))
        a = gaussfunc(X[i - 1], xbar, sigma)
        if abs(f - a) > abs(b - a):
            delta = abs(f - a)
        else:
            delta = abs(b - a)
        if delta > d:
            d = delta
        f = b
    return d, xbar, sigma