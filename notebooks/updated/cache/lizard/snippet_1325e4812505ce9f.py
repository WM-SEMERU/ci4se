def get_month_range(d=None):
    if not d:
        d = timezone.now()
    start = d.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    end = start + relativedelta(months=1)
    return start, end