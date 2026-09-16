def save_object(collection, obj):
    if 'id' not in obj:
        obj.id = uuid()
    id = obj.id
    path = object_path(collection, id)
    temp_path = '%s.temp' % path
    with open(temp_path, 'w') as f:
        data = _serialize(obj)
        f.write(data)
    shutil.move(temp_path, path)
    if id in _db[collection].cache:
        _db[collection].cache[id] = obj
    _update_indexes_for_mutated_object(collection, obj)
    return obj