def throughput(sample, window=1, format='decimal'):
    if isinstance(window, datetime.timedelta):
        window = float(window.days * 86400 + window.seconds)
    elif isinstance(window, six.string_types):
        window = float(window)
    per_second = sample / float(window)
    return _('%s/s') % (filesize(per_second, format=format),)