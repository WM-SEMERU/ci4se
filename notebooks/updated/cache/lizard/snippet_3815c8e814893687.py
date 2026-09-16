def smedian(olist, nobs):
    if nobs:
        rem = nobs % 2
        midpoint = nobs // 2
        me = olist[midpoint]
        if not rem:
            me = 0.5 * (me + olist[midpoint - 1])
        return me
    else:
        return NaN