def timezone(utcoffset):
    hours, seconds = divmod(abs(utcoffset), 3600)
    minutes = round(float(seconds) / 60)
    if utcoffset >= 0:
        sign = '+'
    else:
        sign = '-'
    return '{0}{1:02d}:{2:02d}'.format(sign, int(hours), int(minutes))