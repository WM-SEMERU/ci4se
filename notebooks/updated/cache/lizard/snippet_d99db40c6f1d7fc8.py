def u_grade_ipix(ipix, nside_in, nside_out, nest=False):
    if nside_in == nside_out:
        return ipix
    if not nside_in < nside_out:
        raise ValueError('nside_in must be less than nside_out')
    if nest:
        nest_ipix = ipix
    else:
        nest_ipix = hp.ring2nest(nside_in, ipix)
    factor = (nside_out // nside_in) ** 2
    if np.isscalar(ipix):
        nest_ipix_out = factor * nest_ipix + np.arange(factor)
    else:
        nest_ipix_out = factor * np.asarray(nest_ipix)[:, (np.newaxis)
            ] + np.arange(factor)
    if nest:
        return nest_ipix_out
    else:
        return hp.nest2ring(nside_out, nest_ipix_out)