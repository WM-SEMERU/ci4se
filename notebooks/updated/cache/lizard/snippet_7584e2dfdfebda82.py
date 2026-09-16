def _append_utc_datetime(self, tag, format, ts, precision, header):
    if ts is None:
        t = datetime.datetime.utcnow()
    elif type(ts) is float:
        t = datetime.datetime.utcfromtimestamp(ts)
    else:
        t = ts
    s = t.strftime(format)
    if precision == 3:
        s += '.%03d' % (t.microsecond / 1000)
    elif precision == 6:
        s += '.%06d' % t.microsecond
    elif precision != 0:
        raise ValueError('Precision should be one of 0, 3 or 6 digits')
    return self.append_pair(tag, s, header=header)