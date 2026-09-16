def juldate2date(val):
    ival = int(val)
    dec = val - ival
    try:
        val4 = 4 * ival
        yd = val4 % 1461
        st = 1899
        if yd >= 4:
            st = 1900
        yd1 = yd - 241
        y = val4 // 1461 + st
        if yd1 >= 0:
            q = yd1 // 4 * 5 + 308
            qq = q // 153
            qr = q % 153
        else:
            q = yd // 4 * 5 + 1833
            qq = q // 153
            qr = q % 153
        m = qq % 12 + 1
        d = qr // 5 + 1
    except Exception:
        raise ValueError('Could not convert %s to date' % val)
    if dec:
        dec24 = 24 * dec
        hours = int(dec24)
        minutes = int(60 * (dec24 - hours))
        tot_seconds = 60 * (60 * (dec24 - hours) - minutes)
        seconds = int(tot_seconds)
        microseconds = int(1000000 * (tot_seconds - seconds))
        return datetime(y, m, d, hours, minutes, seconds, microseconds)
    else:
        return date(y, m, d)