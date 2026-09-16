def _normalize_percent_rgb(value):
    percent = value.split('%')[0]
    percent = float(percent) if '.' in percent else int(percent)
    return '0%' if percent < 0 else '100%' if percent > 100 else '{}%'.format(
        percent)