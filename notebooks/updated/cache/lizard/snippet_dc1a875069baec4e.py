def mpfr_mod(rop, x, y, rnd):
    if not mpfr.mpfr_number_p(x) or mpfr.mpfr_nan_p(y) or mpfr.mpfr_zero_p(y):
        return mpfr.mpfr_fmod(rop, x, y, rnd)
    elif mpfr.mpfr_inf_p(y):
        x_negative = mpfr.mpfr_signbit(x)
        y_negative = mpfr.mpfr_signbit(y)
        if mpfr.mpfr_zero_p(x):
            mpfr.mpfr_set_zero(rop, -y_negative)
            return 0
        elif x_negative == y_negative:
            return mpfr.mpfr_set(rop, x, rnd)
        else:
            mpfr.mpfr_set_inf(rop, -y_negative)
            return 0
    x_negative = mpfr.mpfr_signbit(x)
    y_negative = mpfr.mpfr_signbit(y)
    if x_negative == y_negative:
        return mpfr.mpfr_fmod(rop, x, y, rnd)
    else:
        p = max(mpfr.mpfr_get_prec(x), mpfr.mpfr_get_prec(y))
        z = mpfr.Mpfr_t()
        mpfr.mpfr_init2(z, p)
        ternary = mpfr.mpfr_fmod(z, x, y, rnd)
        assert ternary == 0
        if mpfr.mpfr_zero_p(z):
            mpfr.mpfr_set_zero(rop, -y_negative)
            return 0
        else:
            return mpfr.mpfr_add(rop, y, z, rnd)