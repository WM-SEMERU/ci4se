def _get_title_or_id_from_uid(uid):
    try:
        obj = api.get_object_by_uid(uid)
    except api.APIError:
        return '<Deleted {}>'.format(uid)
    title_or_id = api.get_title(obj) or api.get_id(obj)
    return title_or_id