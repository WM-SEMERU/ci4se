def url(route, resource_id=None, pagination=None, **parameters):
    route = route.format(**parameters)
    resource_id_url = '/' + str(resource_id) if resource_id else ''
    query_parameters = ''
    if pagination:
        query_parameters += urlencode(pagination)
    if query_parameters:
        query_parameters = '?' + query_parameters
    return _base_url() + route + resource_id_url + query_parameters