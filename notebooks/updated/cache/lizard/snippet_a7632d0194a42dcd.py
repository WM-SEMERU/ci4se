def re_center(self, x, y, lat, lon):
    state = self.state
    if lat is None or lon is None:
        return
    lat2, lon2 = self.coordinates(x, y)
    distance = mp_util.gps_distance(lat2, lon2, lat, lon)
    bearing = mp_util.gps_bearing(lat2, lon2, lat, lon)
    state.lat, state.lon = mp_util.gps_newpos(state.lat, state.lon, bearing,
        distance)