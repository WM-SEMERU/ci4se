def get_rfc3339(when):
    microseconds = format(when.microsecond, '04d')[:4]
    rfc3339 = '%Y-%m-%dT%H:%M:%S.{}Z'
    return when.strftime(rfc3339.format(microseconds))