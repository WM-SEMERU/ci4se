def get_gpbar(ebar, gbar, v, C, scale_high):
    r
    if C['phiWB'] == 0:
        gpbar = ebar * gbar / sqrt(gbar ** 2 - ebar ** 2)
    else:

        def f0(x):
            gpb = x
            gb = gbar
            eps = C['phiWB'] * (v ** 2 / scale_high ** 2)
            ebar_calc = gb * gpb / sqrt(gb ** 2 + gpb ** 2) * (1 - eps * gb *
                gpb / (gb ** 2 + gpb ** 2))
            return (ebar_calc - ebar).real
        gpbar = scipy.optimize.brentq(f0, 0, 3)
    return gpbar * (1 - C['phiB'] * (v ** 2 / scale_high ** 2))