def get_json(response):
    json_field_or_function = getattr(response, 'json', None)
    if callable(json_field_or_function):
        return response.json()
    else:
        return jsonutils.loads(response.content)