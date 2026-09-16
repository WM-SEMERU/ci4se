def from_rfc3339(value):
    return datetime.datetime.strptime(value, _RFC3339_MICROS).replace(tzinfo
        =pytz.utc)