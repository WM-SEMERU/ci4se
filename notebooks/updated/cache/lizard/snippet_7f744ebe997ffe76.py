def get_pause_duration(recursive_delay=5, default_duration=10):
    try:
        response = requests.get('http://overpass-api.de/api/status')
        status = response.text.split('\n')[3]
        status_first_token = status.split(' ')[0]
    except Exception:
        log('Unable to query http://overpass-api.de/api/status', level=lg.ERROR
            )
        return default_duration
    try:
        available_slots = int(status_first_token)
        pause_duration = 0
    except Exception:
        if status_first_token == 'Slot':
            utc_time_str = status.split(' ')[3]
            utc_time = date_parser.parse(utc_time_str).replace(tzinfo=None)
            pause_duration = math.ceil((utc_time - dt.datetime.utcnow()).
                total_seconds())
            pause_duration = max(pause_duration, 1)
        elif status_first_token == 'Currently':
            time.sleep(recursive_delay)
            pause_duration = get_pause_duration()
        else:
            log('Unrecognized server status: "{}"'.format(status), level=lg
                .ERROR)
            return default_duration
    return pause_duration