def fmod(x, y, context=None):
    return _apply_function_in_current_context(BigFloat, mpfr.mpfr_fmod, (
        BigFloat._implicit_convert(x), BigFloat._implicit_convert(y)), context)