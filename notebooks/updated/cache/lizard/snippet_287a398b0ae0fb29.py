def set_sea_permissions(calendar_id, userid, level):
    url = _make_set_permissions_url(calendar_id, userid, level)
    return _process_resp(url, get_sea_resource(url), _is_permission_set)