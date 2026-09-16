def u_distance_covariance_sqr(x, y, **kwargs):
    if _can_use_fast_algorithm(x, y, **kwargs):
        return _u_distance_covariance_sqr_fast(x, y)
    else:
        return _u_distance_covariance_sqr_naive(x, y, **kwargs)