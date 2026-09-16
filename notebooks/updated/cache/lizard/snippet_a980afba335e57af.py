def datetime_is_iso(date_str):
    try:
        if len(date_str) > 10:
            dt = isodate.parse_datetime(date_str)
        else:
            dt = isodate.parse_date(date_str)
        return True, []
    except:
        return False, ['Datetime provided is not in a valid ISO 8601 format']