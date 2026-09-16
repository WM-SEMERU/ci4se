def list_parameter_ranges(self, parameter, start=None, stop=None, min_gap=
    None, max_gap=None, parameter_cache='realtime'):
    path = '/archive/{}/parameters{}/ranges'.format(self._instance, parameter)
    params = {}
    if start is not None:
        params['start'] = to_isostring(start)
    if stop is not None:
        params['stop'] = to_isostring(stop)
    if min_gap is not None:
        params['minGap'] = int(min_gap * 1000)
    if max_gap is not None:
        params['maxGap'] = int(max_gap * 1000)
    if parameter_cache:
        params['processor'] = parameter_cache
    else:
        params['norealtime'] = True
    response = self._client.get_proto(path=path, params=params)
    message = pvalue_pb2.Ranges()
    message.ParseFromString(response.content)
    ranges = getattr(message, 'range')
    return [ParameterRange(r) for r in ranges]