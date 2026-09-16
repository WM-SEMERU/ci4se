def datetime_from_json(js, manager):
    if js is None:
        return None
    else:
        return dt.datetime(js['year'], js['month'] + 1, js['date'], js[
            'hours'], js['minutes'], js['seconds'], js['milliseconds'] * 1000)