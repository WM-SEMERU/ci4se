def _pdf(self, x, dist, cache):
    return evaluation.evaluate_density(dist, numpy.arcsinh(x), cache=cache
        ) / numpy.sqrt(1 + x * x)