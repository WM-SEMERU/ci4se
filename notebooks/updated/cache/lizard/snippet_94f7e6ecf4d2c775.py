def humanize_timedelta(seconds):
    hours, remainder = divmod(seconds, 3600)
    days, hours = divmod(hours, 24)
    minutes, seconds = divmod(remainder, 60)
    if days:
        result = '{}d'.format(days)
        if hours:
            result += ' {}h'.format(hours)
        if minutes:
            result += ' {}m'.format(minutes)
        return result
    if hours:
        result = '{}h'.format(hours)
        if minutes:
            result += ' {}m'.format(minutes)
        return result
    if minutes:
        result = '{}m'.format(minutes)
        if seconds:
            result += ' {}s'.format(seconds)
        return result
    return '{}s'.format(seconds)