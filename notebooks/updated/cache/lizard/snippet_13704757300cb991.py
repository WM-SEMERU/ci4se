def list_items(action, key, profile_dict=None, api_key=None, opts=None):
    items = salt.utils.json.loads(query(profile_dict=profile_dict, api_key=
        api_key, action=action, opts=opts))
    ret = {}
    for item in items[action]:
        ret[item[key]] = item
    return ret