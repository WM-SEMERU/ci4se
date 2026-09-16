def coth(x, context=None):
    return _apply_function_in_current_context(BigFloat, mpfr.mpfr_coth, (
        BigFloat._implicit_convert(x),), context)