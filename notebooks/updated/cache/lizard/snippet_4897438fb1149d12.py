def decay(ax, p0, pf, A, n, format=None, **kwds):
    r
    if format is None:
        format = 'k-'
    T = sqrt((p0[0] - pf[0]) ** 2 + (p0[1] - pf[1]) ** 2)
    alpha = atan2(pf[1] - p0[1], pf[0] - p0[0])
    x = [(i * T / 400.0) for i in range(401)]
    y = [(A * sin(xi * 2 * pi * n / T)) for xi in x]
    cur_list = [(x, y)]
    cur_list = rotate_and_traslate(cur_list, alpha, p0)
    for curi in cur_list:
        ax.plot(curi[0], curi[1], format, **kwds)