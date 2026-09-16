def expm1(x, context=None):
    return _apply_function_in_current_context(BigFloat, mpfr.mpfr_expm1, (
        BigFloat._implicit_convert(x),), context)