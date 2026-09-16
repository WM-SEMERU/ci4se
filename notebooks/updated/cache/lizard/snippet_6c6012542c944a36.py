def rec_sqrt(x, context=None):
    return _apply_function_in_current_context(BigFloat, mpfr.mpfr_rec_sqrt,
        (BigFloat._implicit_convert(x),), context)