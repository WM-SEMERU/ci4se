def parse_http_date(date):
    MONTHS = 'jan feb mar apr may jun jul aug sep oct nov dec'.split()
    __D = '(?P<day>\\d{2})'
    __D2 = '(?P<day>[ \\d]\\d)'
    __M = '(?P<mon>\\w{3})'
    __Y = '(?P<year>\\d{4})'
    __Y2 = '(?P<year>\\d{2})'
    __T = '(?P<hour>\\d{2}):(?P<min>\\d{2}):(?P<sec>\\d{2})'
    RFC1123_DATE = re.compile('^\\w{3}, %s %s %s %s GMT$' % (__D, __M, __Y,
        __T))
    RFC850_DATE = re.compile('^\\w{6,9}, %s-%s-%s %s GMT$' % (__D, __M,
        __Y2, __T))
    ASCTIME_DATE = re.compile('^\\w{3} %s %s %s %s$' % (__M, __D2, __T, __Y))
    for regex in (RFC1123_DATE, RFC850_DATE, ASCTIME_DATE):
        m = regex.match(date)
        if m is not None:
            break
    else:
        raise ValueError('%r is not in a valid HTTP date format' % date)
    try:
        year = int(m.group('year'))
        if year < 100:
            if year < 70:
                year += 2000
            else:
                year += 1900
        month = MONTHS.index(m.group('mon').lower()) + 1
        day = int(m.group('day'))
        hour = int(m.group('hour'))
        min = int(m.group('min'))
        sec = int(m.group('sec'))
        result = datetime.datetime(year, month, day, hour, min, sec)
        return calendar.timegm(result.utctimetuple())
    except Exception as exc:
        raise ValueError('%r is not a valid date' % date) from exc