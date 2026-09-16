def format_entry(record, show_level=False, colorize=False):
    if show_level:
        log_str = '{}: {}'.format(record.levelname, record.getMessage())
    else:
        log_str = record.getMessage()
    if colorize and record.levelname in LOG_COLORS:
        log_str = '<span color="{}">'.format(LOG_COLORS[record.levelname]
            ) + log_str + '</span>'
    return log_str