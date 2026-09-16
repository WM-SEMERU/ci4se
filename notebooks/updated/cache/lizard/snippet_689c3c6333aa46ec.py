def ynunm(n, m, L):
    out = np.zeros(L, dtype=np.float64)
    tmp1 = 0
    tmp2 = 0
    tmp3 = 0
    tmp4 = 0
    if np.abs(m) <= n:
        out[n] = ynnm(n, m)
        k = n - 2
        if k >= 0:
            tmp1 = (n - k - 1.0) * (n + k + 2.0)
            tmp2 = (n - k - 2.0) * (n + k + 3.0) - 4.0 * m ** 2
            tmp4 = (n - k) * (n + k + 1.0)
            out[k] = (tmp1 + tmp2) * out[k + 2] / tmp4
            for k in xrange(n - 4, -1, -2):
                tmp1 = (n - k - 1.0) * (n + k + 2.0)
                tmp2 = (n - k - 2.0) * (n + k + 3.0) - 4.0 * m ** 2
                tmp3 = (n - k - 3.0) * (n + k + 4.0)
                tmp4 = (n - k) * (n + k + 1.0)
                out[k] = ((tmp1 + tmp2) * out[k + 2] - tmp3 * out[k + 4]
                    ) / tmp4
    return out