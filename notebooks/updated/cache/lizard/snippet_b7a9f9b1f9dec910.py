def attribute_response(resource, name, value):
    if _get_acceptable_response_type() == JSON:
        return _single_attribute_json_response(name, value)
    else:
        return _single_attribute_html_response(resource, name, value)