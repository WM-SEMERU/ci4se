def choose_location_ids(gtfs, stop_ids=None):
    if not stop_ids:
        return [location.gtfs_id for location in gtfs.locations if location
            .station().self_or_children_have_pathways()]
    station_ids = set()
    try:
        for stop_id in stop_ids.split(','):
            station = gtfs.get_location(stop_id).station()
            station_ids.add(station.gtfs_id)
            print('Visualizing station %s' % station.gtfs_id)
    except KeyError:
        raise Exception('Cannot find location with stop_id=%s' % stop_id)
    location_ids = station_ids.copy()
    for station_id in station_ids:
        for child_id in gtfs.get_location(station_id).children:
            location_ids.add(child_id)
            for boarding_area_id in gtfs.get_location(child_id).children:
                location_ids.add(gtfs.get_location(boarding_area_id).gtfs_id)
    return location_ids