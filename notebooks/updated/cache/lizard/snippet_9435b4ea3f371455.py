def parse_date(datestring, default_timezone=UTC):
    if not isinstance(datestring, basestring):
        raise ParseError('Expecting a string %r' % datestring)
    m = ISO8601_REGEX.match(datestring)
    if not m:
        raise ParseError('Unable to parse date string %r' % datestring)
    groups = m.groupdict()
    tz = parse_timezone(groups['timezone'], default_timezone=default_timezone)
    if groups['fraction'] is None:
        groups['fraction'] = 0
    else:
        groups['fraction'] = int(float('0.%s' % groups['fraction']) * 1000000.0
            )
    if groups['hour'] == None and groups['minute'] == None and groups['second'
        ] == None:
        return datetime(int(groups['year']), int(groups['month']), int(
            groups['day']), tzinfo=tz)
    else:
        return datetime(int(groups['year']), int(groups['month']), int(
            groups['day']), int(groups['hour']), int(groups['minute']), int
            (groups['second']), int(groups['fraction']), tz)