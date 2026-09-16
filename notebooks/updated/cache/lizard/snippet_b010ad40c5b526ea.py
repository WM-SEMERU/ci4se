def timezone(self):
    if self._tz is None:
        cen_lat, cen_lon = self.centerLatLon()
        tf = TimezoneFinder()
        tz_name = tf.timezone_at(lng=cen_lon, lat=cen_lat)
        self._tz = timezone(tz_name)
    return self._tz