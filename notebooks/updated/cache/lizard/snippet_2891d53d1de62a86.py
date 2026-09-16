def get_bn(n, mc, dl, F, e):
    mc *= SOLAR2S
    dl *= MPC2S
    omega = 2 * np.pi * F
    amp = n * mc ** (5 / 3) * omega ** (2 / 3) / dl
    ret = -amp * np.sqrt(1 - e ** 2) * (ss.jn(n - 2, n * e) - 2 * ss.jn(n, 
        n * e) + ss.jn(n + 2, n * e))
    return ret