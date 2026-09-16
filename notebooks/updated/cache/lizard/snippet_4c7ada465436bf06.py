def SpiceUDREFN(f):

    @functools.wraps(f)
    def wrapping_udrefn(t1, t2, s1, s2, t):
        result = f(t1, t2, s1, s2)
        t[0] = c_double(result)
    return UDREFN(wrapping_udrefn)