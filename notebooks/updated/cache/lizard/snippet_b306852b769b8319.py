def to_ts(s):
    m = Nginx.DATE_FMT.match(s)
    if m:
        s = m.group(1)
        delta = timedelta(seconds=int(m.group(3)) * (-1 if m.group(2) ==
            '-' else 1))
    else:
        delta = timedelta(seconds=0)
    dt = datetime.strptime(s, '%d/%b/%Y:%H:%M:%S')
    dt += delta
    return dt.strftime('%Y-%m-%dT%H:%M:%SZ')