def transitDurationCircular(P, R_s, R_p, a, i):
    r
    if i is nan:
        i = 90 * aq.deg
    i = i.rescale(aq.rad)
    k = R_p / R_s
    b = a * cos(i) / R_s
    duration = P / pi * arcsin((R_s * sqrt((1 + k) ** 2 - b ** 2) / (a *
        sin(i))).simplified)
    return duration.rescale(aq.min)