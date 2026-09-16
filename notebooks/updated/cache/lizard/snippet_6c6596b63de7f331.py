def get_duration(timestr1, timestr2, units='s'):
    valid_units = ['s', 'min', 'h']
    assert units in valid_units, 'Units must be one of {!s}'.format(valid_units
        )
    duration = gt.timestr_to_seconds(timestr2) - gt.timestr_to_seconds(timestr1
        )
    if units == 's':
        return duration
    elif units == 'min':
        return duration / 60
    else:
        return duration / 3600