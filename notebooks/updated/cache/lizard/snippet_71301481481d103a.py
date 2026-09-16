def from_rfc(datestring, use_dateutil=True):
    if dateutil_available and use_dateutil:
        return parser.parse(datestring)
    else:
        parsed = parsedate(datestring)
        timestamp = time.mktime(parsed)
        return datetime.datetime.fromtimestamp(timestamp)