def singular_subresource(raml_resource, route_name):
    static_parent = get_static_parent(raml_resource, method='POST')
    if static_parent is None:
        return False
    schema = resource_schema(static_parent) or {}
    properties = schema.get('properties', {})
    if route_name not in properties:
        return False
    db_settings = properties[route_name].get('_db_settings', {})
    is_obj = db_settings.get('type') == 'relationship'
    single_obj = not db_settings.get('uselist', True)
    return is_obj and single_obj