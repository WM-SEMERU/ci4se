def _parse(partial_dt):
    dt = None
    try:
        if isinstance(partial_dt, datetime):
            dt = partial_dt
        if isinstance(partial_dt, date):
            dt = _combine_date_time(partial_dt, time(0, 0, 0))
        if isinstance(partial_dt, time):
            dt = _combine_date_time(date.today(), partial_dt)
        if isinstance(partial_dt, (int, float)):
            dt = datetime.fromtimestamp(partial_dt)
        if isinstance(partial_dt, (str, bytes)):
            dt = parser.parse(partial_dt, default=timezone.now())
        if dt is not None and timezone.is_naive(dt):
            dt = timezone.make_aware(dt)
        return dt
    except ValueError:
        return None