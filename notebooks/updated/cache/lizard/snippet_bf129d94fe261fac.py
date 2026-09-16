def EvalBinomialPmf(k, n, p):
    return scipy.stats.binom.pmf(k, n, p)