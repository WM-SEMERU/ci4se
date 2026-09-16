def get_resource(collection, key):
    resource = retrieve_resource(collection, key)
    _validate(endpoint_class(collection), request.method, resource)
    return resource_response(resource)