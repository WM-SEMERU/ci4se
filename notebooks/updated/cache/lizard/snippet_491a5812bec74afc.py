def ynnm(n, m):
    a = 1.0 / np.sqrt(4.0 * np.pi)
    pm = np.abs(m)
    out = 0.0
    if n < pm:
        out = 0.0
    elif n == 0:
        out = a
    else:
        out = a
        for k in xrange(1, n + 1):
            out *= np.sqrt((2.0 * k + 1.0) / 8.0 / k)
        if n != pm:
            for k in xrange(n - 1, pm - 1, -1):
                out *= np.sqrt((n + k + 1.0) / (n - k))
    return out