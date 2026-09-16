def ccor2(alt, r, h1, zh, h2):
    e1 = (alt - zh) / h1
    e2 = (alt - zh) / h2
    if e1 > 70.0 or e2 > 70:
        return 1.0
    if e1 < -70 and e2 < -70:
        return exp(r)
    ex1 = exp(e1)
    ex2 = exp(e2)
    ccor2v = r / (1.0 + 0.5 * (ex1 + ex2))
    return exp(ccor2v)