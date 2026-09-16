def next_cron(previous_dt: datetime, *, month: Union[None, set, int]=None,
    day: Union[None, set, int]=None, weekday: Union[None, set, int, str]=
    None, hour: Union[None, set, int]=None, minute: Union[None, set, int]=
    None, second: Union[None, set, int]=0, microsecond: int=123456):
    dt = previous_dt + timedelta(seconds=1)
    if isinstance(weekday, str):
        weekday = weekdays.index(weekday.lower())
    options = dict(month=month, day=day, weekday=weekday, hour=hour, minute
        =minute, second=second, microsecond=microsecond)
    while True:
        next_dt = _get_next_dt(dt, options)
        if next_dt is None:
            return dt
        dt = next_dt