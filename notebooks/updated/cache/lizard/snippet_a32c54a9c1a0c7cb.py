def extract_bus_routine(page):
    if not isinstance(page, pq):
        page = pq(page)
    stations = extract_stations(page)
    return {'name': extract_routine_name(page), 'stations': stations,
        'current': extract_current_routine(page, stations)}