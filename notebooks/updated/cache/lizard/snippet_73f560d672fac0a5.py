def ccor(alt, r, h1, zh):
    e = (alt - zh) / h1
    if e > 70.0:
        return 1.0
    elif e < -70.0:
        return exp(r)
    ex = exp(e)
    e = r / (1.0 + ex)
    return exp(e)