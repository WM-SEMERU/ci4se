def cos(x, context=None):
    return _apply_function_in_current_context(BigFloat, mpfr.mpfr_cos, (
        BigFloat._implicit_convert(x),), context)