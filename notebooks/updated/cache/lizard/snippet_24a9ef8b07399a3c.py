def future_date(end='+30d'):
    return lambda n, f: f.future_date(end_date=end, tzinfo=get_timezone())