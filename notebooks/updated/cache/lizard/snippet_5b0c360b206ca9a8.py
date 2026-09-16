def timestamp_from_RFC3339(RFC3339):
    dt = dateutil.parser.parse(RFC3339)
    if hasattr(dt.tzinfo, '_offset'):
        timezone = dt.tzinfo._offset.total_seconds()
    else:
        timezone = 'utc'
    timestamp = TimeStamp(at=dt.timestamp(), timezone=timezone)
    return timestamp