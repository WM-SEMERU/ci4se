def data(self, where, start, end, archiver='', timeout=DEFAULT_TIMEOUT):
    return self.query('select data in ({0}, {1}) where {2}'.format(start,
        end, where), archiver, timeout).get('timeseries', {})