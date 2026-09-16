def get_resource(remote):
    cached_resource = session.pop('cern_resource', None)
    if cached_resource:
        return cached_resource
    response = remote.get(REMOTE_APP_RESOURCE_API_URL)
    dict_response = get_dict_from_response(response)
    session['cern_resource'] = dict_response
    return dict_response