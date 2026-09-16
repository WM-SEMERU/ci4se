def default_validity_start():
    start = datetime.now() - timedelta(days=1)
    return start.replace(hour=0, minute=0, second=0, microsecond=0)