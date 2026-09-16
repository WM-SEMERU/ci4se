def optimize_providers(providers):
    tmp_providers = {}
    optimized_providers = {}
    for name, data in six.iteritems(providers):
        if 'location' not in data:
            data['location'] = DEFAULT_LOCATION
        if data['location'] not in tmp_providers:
            tmp_providers[data['location']] = {}
        creds = data['id'], data['key']
        if creds not in tmp_providers[data['location']]:
            tmp_providers[data['location']][creds] = {'name': name, 'data':
                data}
    for location, tmp_data in six.iteritems(tmp_providers):
        for creds, data in six.iteritems(tmp_data):
            _id, _key = creds
            _name = data['name']
            _data = data['data']
            if _name not in optimized_providers:
                optimized_providers[_name] = _data
    return optimized_providers