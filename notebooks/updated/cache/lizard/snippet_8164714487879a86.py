def human_readable_delta(start, end):
    start_date = datetime.datetime.fromtimestamp(start)
    end_date = datetime.datetime.fromtimestamp(end)
    delta = end_date - start_date
    result = []
    if delta.days > 0:
        result.append('%d days' % (delta.days,))
    if delta.seconds > 0:
        hours = int(delta.seconds / 3600)
        if hours > 0:
            result.append('%d hours' % (hours,))
        minutes = int((delta.seconds - hours * 3600) / 60)
        if minutes:
            result.append('%d minutes' % (minutes,))
        seconds = delta.seconds % 60
        if seconds > 0:
            result.append('%d seconds' % (seconds,))
    if result:
        return ', '.join(result)
    return 'super fast'