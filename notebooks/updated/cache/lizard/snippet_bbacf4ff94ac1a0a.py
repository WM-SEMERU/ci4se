def precip(self, start, end, **kwargs):
    r
    self._check_geo_param(kwargs)
    kwargs['start'] = start
    kwargs['end'] = end
    kwargs['token'] = self.token
    return self._get_response('stations/precipitation', kwargs)