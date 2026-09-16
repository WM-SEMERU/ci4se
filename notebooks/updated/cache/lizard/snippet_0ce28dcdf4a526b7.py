def lessequal(x, y):
    x = BigFloat._implicit_convert(x)
    y = BigFloat._implicit_convert(y)
    return mpfr.mpfr_lessequal_p(x, y)