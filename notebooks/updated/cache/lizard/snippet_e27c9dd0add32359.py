def _make_datetime(s):
    r
    s = bytearray(s)
    year, month, day, hour, minute, second, cs = s
    if year < 70:
        year += 100
    return datetime(1900 + year, month, day, hour, minute, second, 10000 * cs)