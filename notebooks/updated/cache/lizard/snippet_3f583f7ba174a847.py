def closest_eere(latitude, longitude):
    with open(env.SRC_PATH + '/eere_meta.csv') as eere_meta:
        stations = csv.DictReader(eere_meta)
        d = 9999
        station_code = ''
        station_name = ''
        for station in stations:
            new_dist = great_circle((latitude, longitude), (float(station[
                'latitude']), float(station['longitude']))).miles
            if new_dist <= d:
                d = new_dist
                station_code = station['station_code']
                station_name = station['weather_station']
        return station_code, station_name
    raise KeyError('station not found')