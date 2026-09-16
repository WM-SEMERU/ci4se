def survival(value=t, lam=lam, f=failure):
    return sum(f * log(lam) - lam * value)