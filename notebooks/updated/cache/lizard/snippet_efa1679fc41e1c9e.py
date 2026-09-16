def _normalize(parsed, **options):
    if options.get('exact'):
        return parsed
    if isinstance(parsed, time):
        now = options['now'] or datetime.now()
        return datetime(now.year, now.month, now.day, parsed.hour, parsed.
            minute, parsed.second, parsed.microsecond)
    elif isinstance(parsed, date) and not isinstance(parsed, datetime):
        return datetime(parsed.year, parsed.month, parsed.day)
    return parsed