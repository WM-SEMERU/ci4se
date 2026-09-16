def humanize_hours(total_hours, frmt=
    '{hours:02d}:{minutes:02d}:{seconds:02d}', negative_frmt=None):
    seconds = int(float(total_hours) * 3600)
    return humanize_seconds(seconds, frmt, negative_frmt)