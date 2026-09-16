def _tzstr(self, sep=':'):
    off = self.utcoffset()
    if off is not None:
        if off.days < 0:
            sign = '-'
            off = -off
        else:
            sign = '+'
        hh, mm = divmod(off, timedelta(hours=1))
        assert not mm % timedelta(minutes=1), 'whole minute'
        mm //= timedelta(minutes=1)
        assert 0 <= hh < 24
        off = '%s%02d%s%02d' % (sign, hh, sep, mm)
    return off