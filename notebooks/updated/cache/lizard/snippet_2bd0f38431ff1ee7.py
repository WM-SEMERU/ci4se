def eta_letters(seconds):
    final_days, final_hours, final_minutes, final_seconds = 0, 0, 0, seconds
    if final_seconds >= 86400:
        final_days = int(final_seconds / 86400.0)
        final_seconds -= final_days * 86400
    if final_seconds >= 3600:
        final_hours = int(final_seconds / 3600.0)
        final_seconds -= final_hours * 3600
    if final_seconds >= 60:
        final_minutes = int(final_seconds / 60.0)
        final_seconds -= final_minutes * 60
    final_seconds = int(math.ceil(final_seconds))
    if final_days:
        template = '{1:d}d {2:d}h {3:02d}m {4:02d}s'
    elif final_hours:
        template = '{2:d}h {3:02d}m {4:02d}s'
    elif final_minutes:
        template = '{3:02d}m {4:02d}s'
    else:
        template = '{4:02d}s'
    return template.format(final_days, final_hours, final_minutes,
        final_seconds)