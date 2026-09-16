def interpolate_data(self, data, limit, method):
    data = data.interpolate(how='index', limit=limit, method=method)
    return data