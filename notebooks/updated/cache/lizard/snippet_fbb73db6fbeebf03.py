def parse_timespan(timedef):
    if isinstance(timedef, int):
        return timedef
    converter_order = 'w', 'd', 'h', 'm', 's'
    converters = {'w': 604800, 'd': 86400, 'h': 3600, 'm': 60, 's': 1}
    timedef = timedef.lower()
    if timedef.isdigit():
        return int(timedef)
    elif len(timedef) == 0:
        return 0
    seconds = -1
    for spec in converter_order:
        timedef = timedef.split(spec)
        if len(timedef) == 1:
            timedef = timedef[0]
            continue
        elif len(timedef) > 2 or not timedef[0].isdigit():
            seconds = -1
            break
        adjustment = converters[spec]
        seconds = max(seconds, 0)
        seconds += int(timedef[0]) * adjustment
        timedef = timedef[1]
        if not len(timedef):
            break
    if seconds < 0:
        raise ValueError('invalid time format')
    return seconds