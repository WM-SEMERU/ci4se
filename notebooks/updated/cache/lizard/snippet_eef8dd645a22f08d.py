def run_friedman_smooth(x, y, span):
    N = len(x)
    weight = numpy.ones(N)
    results = numpy.zeros(N)
    residuals = numpy.zeros(N)
    mace.smooth(x, y, weight, span, 1, 1e-07, results, residuals)
    return results, residuals