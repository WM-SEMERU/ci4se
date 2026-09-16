def get_time_period(value):
    for time_period in TimePeriod:
        if time_period.period == value:
            return time_period
    raise ValueError('{} is not a valid TimePeriod'.format(value))