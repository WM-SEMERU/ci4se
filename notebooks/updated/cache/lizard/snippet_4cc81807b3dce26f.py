def _check_date_format(date, api):
    try:
        datetime.datetime.strptime(date, api.DATE_FORMAT)
    except ValueError:
        raise ValueError("Date '{}' does not conform to API format: {}".
            format(date, api.DATE_FORMAT))