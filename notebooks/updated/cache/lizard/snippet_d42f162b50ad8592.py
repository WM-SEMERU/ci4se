def deactivate_resource(cls, id):
    r
    try:
        this_resource = cls.nodes.get(id=id, active=True)
        this_resource.deactivate()
        r = make_response('')
        r.headers['Content-Type'] = 'application/vnd.api+json; charset=utf-8'
        r.status_code = http_error_codes.NO_CONTENT
    except DoesNotExist:
        r = application_codes.error_response([application_codes.
            RESOURCE_NOT_FOUND])
    return r