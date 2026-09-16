def calculate_acl(data, m=5, dtype=int):
    r
    if dtype not in [int, float]:
        raise ValueError('The dtype must be either int or float.')
    if len(data) < 2:
        return 1
    acf = calculate_acf(data)
    cacf = 2 * acf.numpy().cumsum() - 1
    win = m * cacf <= numpy.arange(len(cacf))
    if win.any():
        acl = cacf[numpy.where(win)[0][0]]
        if dtype == int:
            acl = int(numpy.ceil(acl))
    else:
        acl = numpy.inf
    return acl