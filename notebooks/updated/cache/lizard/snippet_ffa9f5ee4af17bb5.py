def get_an(n, mc, dl, F, e):
    mc *= SOLAR2S
    dl *= MPC2S
    omega = 2 * np.pi * F
    amp = n * mc ** (5 / 3) * omega ** (2 / 3) / dl
    ret = -amp * (ss.jn(n - 2, n * e) - 2 * e * ss.jn(n - 1, n * e) + 2 / n *
        ss.jn(n, n * e) + 2 * e * ss.jn(n + 1, n * e) - ss.jn(n + 2, n * e))
    return ret