def from_timedelta(cls, timedelta):
    from math import ceil
    units = ceil(timedelta.total_seconds() / cls.time_unit)
    return cls.create(units)