def process_date_from_to_options(options, to_datetime=False, default_dt_to=
    False):
    start_time = datetime.datetime.now()
    if options.get('last_week'):
        dt_from = start_time - datetime.timedelta(days=7)
        dt_to = start_time
    elif options.get('last_day'):
        dt_from = start_time - datetime.timedelta(days=1)
        dt_to = start_time
    elif options.get('last_2hours'):
        dt_from = start_time - datetime.timedelta(hours=2)
        dt_to = start_time
    else:
        from_str = options.get('from')
        if from_str:
            try:
                dt_from = iso_to_datetime(from_str)
            except:
                dt_from = iso_to_date(from_str)
        else:
            dt_from = None
        to_str = options.get('to')
        if to_str:
            try:
                dt_to = iso_to_datetime(to_str)
            except:
                dt_to = iso_to_date(to_str)
        else:
            dt_to = None
    if default_dt_to and not dt_to:
        dt_to = datetime.datetime(2100, 1, 1)
    if to_datetime:
        if isinstance(dt_from, datetime.date):
            dt_from = date_to_datetime(dt_from)
        if isinstance(dt_to, datetime.date):
            dt_to = date_to_datetime_lte(dt_to)
    return dt_from, dt_to