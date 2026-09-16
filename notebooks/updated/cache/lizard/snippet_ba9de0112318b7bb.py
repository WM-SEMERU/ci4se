def _parse_odata_timestamp(in_date):
    timestamp = int(in_date.replace('/Date(', '').replace(')/', ''))
    seconds = timestamp // 1000
    ms = timestamp % 1000
    return datetime.utcfromtimestamp(seconds) + timedelta(milliseconds=ms)