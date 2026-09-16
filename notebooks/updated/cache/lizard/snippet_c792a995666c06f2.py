def get_relationship(self, session, query, api_type, obj_id, rel_key):
    resource = self._fetch_resource(session, api_type, obj_id, Permissions.VIEW
        )
    if rel_key not in resource.__jsonapi_map_to_py__.keys():
        raise RelationshipNotFoundError(resource, resource, rel_key)
    py_key = resource.__jsonapi_map_to_py__[rel_key]
    relationship = self._get_relationship(resource, py_key, Permissions.VIEW)
    response = JSONAPIResponse()
    related = get_rel_desc(resource, relationship.key, RelationshipActions.GET
        )(resource)
    if relationship.direction == MANYTOONE:
        if related is None:
            response.data['data'] = None
        else:
            try:
                response.data['data'] = self._render_short_instance(related)
            except PermissionDeniedError:
                response.data['data'] = None
    else:
        response.data['data'] = []
        for item in related:
            try:
                response.data['data'].append(self._render_short_instance(item))
            except PermissionDeniedError:
                continue
    return response