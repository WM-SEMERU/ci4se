def pickle_sequence(objects):
    cache = {}
    out = []
    for obj in objects:
        obj_id = id(obj)
        if obj_id not in cache:
            if isinstance(obj, Pickled):
                cache[obj_id] = obj
            else:
                cache[obj_id] = Pickled(obj)
        out.append(cache[obj_id])
    return out