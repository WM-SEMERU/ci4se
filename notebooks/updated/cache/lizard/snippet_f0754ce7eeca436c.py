def get_seconds_until_next_quarter(now=None):
    if now is None:
        now = arrow.utcnow()
    return 899 - (now - now.replace(minute=now.minute // 15 * 15, second=0,
        microsecond=0)).seconds