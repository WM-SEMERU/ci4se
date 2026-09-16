def valid_daily_max_temperature(comp, units='K'):
    r

    @wraps(comp)
    def func(tasmax, *args, **kwds):
        check_valid_temperature(tasmax, units)
        check_valid(tasmax, 'cell_methods', 'time: maximum within days')
        return comp(tasmax, *args, **kwds)
    return func