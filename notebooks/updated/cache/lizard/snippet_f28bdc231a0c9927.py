def optimized(code, silent=True, ignore_errors=True):
    return constant_fold(code, silent=silent, ignore_errors=ignore_errors)