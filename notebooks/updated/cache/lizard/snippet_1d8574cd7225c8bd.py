def timezone(self, lat, lon, datetime, language=None, sensor=None):
    parameters = dict(location='%f,%f' % (lat, lon), timestamp=
        unixtimestamp(datetime), language=language, sensor=sensor)
    return self._make_request(self.TIMEZONE_URL, parameters, None)