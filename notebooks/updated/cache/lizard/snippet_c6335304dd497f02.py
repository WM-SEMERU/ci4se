def _item_list(profile=None):
    g_client = _auth(profile)
    ret = []
    for item in g_client.items.list():
        ret.append(item.__dict__)
    return ret