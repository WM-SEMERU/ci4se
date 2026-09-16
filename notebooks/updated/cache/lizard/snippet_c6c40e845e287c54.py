def iso8601_date(s):
    try:
        return datetime.datetime.strptime(s, ISO8601_DATE_FORMAT).replace(
            tzinfo=pytz.utc).date()
    except (TypeError, ValueError):
        return s