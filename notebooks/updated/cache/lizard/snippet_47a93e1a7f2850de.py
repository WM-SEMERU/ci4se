def getdateByTimezone(cDateUTC, timezone=None):
    dt = cDateUTC[0:19]
    if timezone and len(cDateUTC) == 25:
        tz = cDateUTC[19:25]
        tz = int(tz.split(':')[0])
        dt = datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S')
        dt = dt - timedelta(hours=tz)
        dt = pytz.utc.localize(dt)
        dt = timezone.normalize(dt)
        dt = dt.strftime('%Y-%m-%dT%H:%M:%S')
    cDt = dt[0:10].split('-')
    cDt.reverse()
    return '/'.join(cDt), dt[11:16]