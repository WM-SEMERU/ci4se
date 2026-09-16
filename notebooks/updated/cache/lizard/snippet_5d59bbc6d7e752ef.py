def _clean_frequency(frequency):
    if isinstance(frequency, int):
        return frequency
    elif isinstance(frequency, datetime.timedelta):
        return int(frequency.total_seconds())
    raise ValueError('Invalid frequency {!r}'.format(frequency))