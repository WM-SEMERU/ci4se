def format_size(num, format_str='{num:.1f} {unit}'):
    for unit in ('B', 'KiB', 'MiB', 'GiB'):
        if -1024 < num < 1024:
            return format_str.format(num=num, unit=unit)
        num /= 1024.0
    return format_str.format(num=num, unit='TiB')