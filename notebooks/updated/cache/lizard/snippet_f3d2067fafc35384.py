def change_uid(bridge_id, new_uwnetid, no_custom_fields=True):
    url = author_id_url(bridge_id)
    if not no_custom_fields:
        url += '?%s' % CUSTOM_FIELD
    resp = patch_resource(url, '{"user":{"uid":"%s@uw.edu"}}' % new_uwnetid)
    return _process_json_resp_data(resp, no_custom_fields=no_custom_fields)