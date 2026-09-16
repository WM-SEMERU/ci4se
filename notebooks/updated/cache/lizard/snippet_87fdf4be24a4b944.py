def stringToDateTime(s, tzinfo=None):
    try:
        year = int(s[0:4])
        month = int(s[4:6])
        day = int(s[6:8])
        hour = int(s[9:11])
        minute = int(s[11:13])
        second = int(s[13:15])
        if len(s) > 15:
            if s[15] == 'Z':
                tzinfo = getTzid('UTC')
    except:
        raise ParseError("'{0!s}' is not a valid DATE-TIME".format(s))
    year = year and year or 2000
    if tzinfo is not None and hasattr(tzinfo, 'localize'):
        return tzinfo.localize(datetime.datetime(year, month, day, hour,
            minute, second))
    return datetime.datetime(year, month, day, hour, minute, second, 0, tzinfo)