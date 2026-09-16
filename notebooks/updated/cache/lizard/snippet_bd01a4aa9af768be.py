def parse_isoformat(timestamp):
    if len(timestamp) == 20:
        zone = TzOffset('+00:00')
        timestamp = timestamp[:-1]
    elif len(timestamp) == 24:
        zone = TzOffset('%s:%s' % (timestamp[-5:-2], timestamp[-2:]))
        timestamp = timestamp[:-5]
    elif len(timestamp) == 25:
        zone = TzOffset(timestamp[-6:])
        timestamp = timestamp[:-6]
    timestamp = Timestamp.strptime(timestamp, '%Y-%m-%dT%H:%M:%S')
    timestamp = timestamp.replace(tzinfo=zone)
    return timestamp