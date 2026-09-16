def f2tc(f, base=25):
    try:
        f = int(f)
    except:
        return '--:--:--:--'
    hh = int(f / base / 3600)
    mm = int(f / base / 60 - hh * 60)
    ss = int(f / base - hh * 3600 - mm * 60)
    ff = int(f - hh * 3600 * base - mm * 60 * base - ss * base)
    return '{:02d}:{:02d}:{:02d}:{:02d}'.format(hh, mm, ss, ff)