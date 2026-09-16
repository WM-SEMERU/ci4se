def _fetch_resource(self, session, api_type, obj_id, permission):
    if api_type not in self.models.keys():
        raise ResourceTypeNotFoundError(api_type)
    obj = session.query(self.models[api_type]).get(obj_id)
    if obj is None:
        raise ResourceNotFoundError(self.models[api_type], obj_id)
    check_permission(obj, None, permission)
    return obj