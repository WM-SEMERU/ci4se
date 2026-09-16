def beta(a, b):
    beta = math.exp(math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b))
    return beta