def get_grading_status(section_id, act_as=None):
    url = '{}/{}'.format(url_prefix, quote(section_id))
    headers = {}
    if act_as is not None:
        headers['X-UW-Act-as'] = act_as
    response = get_resource(url, headers)
    return _object_from_json(url, response)