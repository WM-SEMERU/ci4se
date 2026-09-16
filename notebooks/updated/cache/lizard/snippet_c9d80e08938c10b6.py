def get_pegasus_to_nice_fn(*args, **kwargs):
    if args or kwargs:
        warnings.warn(
            'Deprecation warning: get_pegasus_to_nice_fn does not need / use parameters anymore'
            )

    def p2n0(u, w, k, z):
        return 0, w - 1 if u else z, z if u else w, u, k - 4 if u else k - 4

    def p2n1(u, w, k, z):
        return 1, w - 1 if u else z, z if u else w, u, k if u else k - 8

    def p2n2(u, w, k, z):
        return 2, w if u else z, z if u else w - 1, u, k - 8 if u else k

    def p2n(u, w, k, z):
        return [p2n0, p2n1, p2n2][(2 - u - (2 * u - 1) * (k // 4)) % 3](u,
            w, k, z)
    return p2n