def chisqprob(x, df):
    if x <= 0:
        return 1.0
    if x == 0:
        return 0.0
    if df <= 0:
        raise ValueError('Domain error.')
    if x < 1.0 or x < df:
        return 1.0 - _igam(0.5 * df, 0.5 * x)
    return _igamc(0.5 * df, 0.5 * x)