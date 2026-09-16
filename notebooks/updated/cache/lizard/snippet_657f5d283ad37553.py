def EvalPoissonPmf(k, lam):
    return lam ** k * math.exp(-lam) / math.factorial(k)