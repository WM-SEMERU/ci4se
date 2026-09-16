def _parse_time_to_freeze(time_to_freeze_str):
    if time_to_freeze_str is None:
        time_to_freeze_str = datetime.datetime.utcnow()
    if isinstance(time_to_freeze_str, datetime.datetime):
        time_to_freeze = time_to_freeze_str
    elif isinstance(time_to_freeze_str, datetime.date):
        time_to_freeze = datetime.datetime.combine(time_to_freeze_str,
            datetime.time())
    elif isinstance(time_to_freeze_str, datetime.timedelta):
        time_to_freeze = datetime.datetime.utcnow() + time_to_freeze_str
    else:
        time_to_freeze = parser.parse(time_to_freeze_str)
    return convert_to_timezone_naive(time_to_freeze)