def _ppf(self, q, left, right, cache):
    left = evaluation.get_inverse_cache(left, cache)
    right = evaluation.get_inverse_cache(right, cache)
    if isinstance(left, Dist):
        if isinstance(right, Dist):
            raise StochasticallyDependentError(
                'under-defined distribution {} or {}'.format(left, right))
    elif not isinstance(right, Dist):
        return left ** right
    else:
        out = evaluation.evaluate_inverse(right, q, cache=cache)
        out = numpy.where(left < 0, 1 - out, out)
        out = left ** out
        return out
    right = right + numpy.zeros(q.shape)
    q = numpy.where(right < 0, 1 - q, q)
    out = evaluation.evaluate_inverse(left, q, cache=cache) ** right
    return out