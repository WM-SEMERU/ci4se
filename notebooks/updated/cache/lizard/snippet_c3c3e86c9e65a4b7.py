def parse_datetime_aware(s, tz=None):
    assert settings.USE_TZ
    if isinstance(s, datetime.datetime):
        return s
    d = parse_datetime(s)
    if d is None:
        raise ValueError
    return timezone.make_aware(d, tz or timezone.get_current_timezone())