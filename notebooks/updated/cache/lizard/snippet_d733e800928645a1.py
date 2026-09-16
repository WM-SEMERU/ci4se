def obrientransform(*args):
    TINY = 1e-10
    k = len(args)
    n = [0.0] * k
    v = [0.0] * k
    m = [0.0] * k
    nargs = []
    for i in range(k):
        nargs.append(copy.deepcopy(args[i]))
        n[i] = float(len(nargs[i]))
        v[i] = var(nargs[i])
        m[i] = mean(nargs[i])
    for j in range(k):
        for i in range(n[j]):
            t1 = (n[j] - 1.5) * n[j] * (nargs[j][i] - m[j]) ** 2
            t2 = 0.5 * v[j] * (n[j] - 1.0)
            t3 = (n[j] - 1.0) * (n[j] - 2.0)
            nargs[j][i] = (t1 - t2) / float(t3)
    check = 1
    for j in range(k):
        if v[j] - mean(nargs[j]) > TINY:
            check = 0
    if check != 1:
        raise ValueError('Problem in obrientransform.')
    else:
        return nargs