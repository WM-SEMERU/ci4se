def get_(key, recurse=False, profile=None, **kwargs):
    client = __utils__['etcd_util.get_conn'](__opts__, profile, **kwargs)
    if recurse:
        return client.tree(key)
    else:
        return client.get(key, recurse=recurse)