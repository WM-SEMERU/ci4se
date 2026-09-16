def move_datetime_week(dt, direction, num_shifts):
    delta = relativedelta(weeks=+num_shifts)
    return _move_datetime(dt, direction, delta)