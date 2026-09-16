def _json_body_(cls):
    json = []
    for series_name, data in six.iteritems(cls._datapoints):
        json.append({'name': series_name, 'columns': cls._fields, 'points':
            [[getattr(point, k) for k in cls._fields] for point in data]})
    return json