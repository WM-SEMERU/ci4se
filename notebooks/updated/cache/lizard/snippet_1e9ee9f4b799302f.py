def humanize(number):
    units = 'bytes', 'KiB', 'MiB', 'GiB', 'TiB'
    base = 1024
    if number is None:
        return None
    pow = int(math.log(number, base)) if number > 0 else 0
    pow = min(pow, len(units) - 1)
    mantissa = number / base ** pow
    return '%.4g %s' % (mantissa, units[pow])