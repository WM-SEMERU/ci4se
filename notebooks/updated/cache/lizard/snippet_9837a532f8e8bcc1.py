def get_lat_lon_time_from_nmea(nmea_file, local_time=True):
    with open(nmea_file, 'r') as f:
        lines = f.readlines()
        lines = [l.rstrip('\n\r') for l in lines]
    for l in lines:
        if 'GPRMC' in l:
            data = pynmea2.parse(l)
            date = data.datetime.date()
            break
    points = []
    for l in lines:
        if 'GPRMC' in l:
            data = pynmea2.parse(l)
            date = data.datetime.date()
        if '$GPGGA' in l:
            data = pynmea2.parse(l)
            timestamp = datetime.datetime.combine(date, data.timestamp)
            lat, lon, alt = data.latitude, data.longitude, data.altitude
            points.append((timestamp, lat, lon, alt))
    points.sort()
    return points