def closest_noaa(latitude, longitude):
    with open(env.SRC_PATH + '/inswo-stns.txt') as index:
        index.readline()
        index.readline()
        min_dist = 9999
        station_name = ''
        station_name = ''
        for line in index:
            try:
                i = parse_noaa_line(line)
                new_dist = great_circle((latitude, longitude), (float(i[
                    'LAT']), float(i['LON']))).miles
            except:
                logger.error(line)
                raise IOError('Inventory Issue')
            if new_dist < min_dist:
                min_dist = new_dist
                station_name = i['station_name']
                station_code = i['station_code']
        index.close()
        return station_code, station_name
    raise KeyError('station not found')