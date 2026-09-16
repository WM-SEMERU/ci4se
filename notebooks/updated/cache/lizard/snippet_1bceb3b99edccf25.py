def resource_response(resource, depth=0):
    if _get_acceptable_response_type() == JSON:
        depth = 0
        if 'expand' in request.args:
            depth = 1
        return _single_resource_json_response(resource, depth)
    else:
        return _single_resource_html_response(resource)