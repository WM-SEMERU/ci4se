def group_by(resources, key):
    resource_map = {}
    parts = key.split('.')
    for r in resources:
        v = r
        for k in parts:
            v = v.get(k)
            if not isinstance(v, dict):
                break
        resource_map.setdefault(v, []).append(r)
    return resource_map