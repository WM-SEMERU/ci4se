def find_by_name(collection, name, exact=True):
    params = {'filter[]': ['name==%s' % name]}
    found = collection.index(params=params)
    if not exact and len(found) > 0:
        return found
    for f in found:
        if f.soul['name'] == name:
            return f