def weighted_average(rule, artifact):
    e = 0
    w = 0
    for i in range(len(rule.R)):
        r = rule.R[i](artifact)
        if r is not None:
            e += r * rule.W[i]
            w += abs(rule.W[i])
    if w == 0.0:
        return 0.0
    return e / w