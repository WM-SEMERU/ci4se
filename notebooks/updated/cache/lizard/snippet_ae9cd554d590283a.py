def distance_correlation_sqr(x, y, **kwargs):
    if _can_use_fast_algorithm(x, y, **kwargs):
        return _distance_correlation_sqr_fast(x, y)
    else:
        return _distance_correlation_sqr_naive(x, y, **kwargs)