def wilcoxont(x, y):
    if len(x) != len(y):
        raise ValueError('Unequal N in wilcoxont.  Aborting.')
    d = []
    for i in range(len(x)):
        diff = x[i] - y[i]
        if diff != 0:
            d.append(diff)
    count = len(d)
    absd = map(abs, d)
    absranked = rankdata(absd)
    r_plus = 0.0
    r_minus = 0.0
    for i in range(len(absd)):
        if d[i] < 0:
            r_minus = r_minus + absranked[i]
        else:
            r_plus = r_plus + absranked[i]
    wt = min(r_plus, r_minus)
    mn = count * (count + 1) * 0.25
    se = math.sqrt(count * (count + 1) * (2.0 * count + 1.0) / 24.0)
    z = math.fabs(wt - mn) / se
    prob = 2 * (1.0 - zprob(abs(z)))
    return wt, prob