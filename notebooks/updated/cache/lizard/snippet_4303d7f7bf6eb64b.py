def interval(value=None, unit='s', years=None, quarters=None, months=None,
    weeks=None, days=None, hours=None, minutes=None, seconds=None,
    milliseconds=None, microseconds=None, nanoseconds=None):
    if value is not None:
        if isinstance(value, datetime.timedelta):
            unit = 's'
            value = int(value.total_seconds())
        elif not isinstance(value, int):
            raise ValueError('Interval value must be an integer')
    else:
        kwds = [('Y', years), ('Q', quarters), ('M', months), ('W', weeks),
            ('D', days), ('h', hours), ('m', minutes), ('s', seconds), (
            'ms', milliseconds), ('us', microseconds), ('ns', nanoseconds)]
        defined_units = [(k, v) for k, v in kwds if v is not None]
        if len(defined_units) != 1:
            raise ValueError('Exactly one argument is required')
        unit, value = defined_units[0]
    value_type = literal(value).type()
    type = dt.Interval(unit, value_type)
    return literal(value, type=type).op().to_expr()