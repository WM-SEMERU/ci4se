def _ensure_object_id(cls, id):
    if isinstance(id, ObjectId):
        return id
    if isinstance(id, basestring) and OBJECTIDEXPR.match(id):
        return ObjectId(id)
    return id