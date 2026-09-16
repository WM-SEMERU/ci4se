def binomial_prefactor(s, ia, ib, xpa, xpb):
    total = 0
    for t in range(s + 1):
        if s - ia <= t <= ib:
            total += binomial(ia, s - t) * binomial(ib, t) * pow(xpa, ia -
                s + t) * pow(xpb, ib - t)
    return total