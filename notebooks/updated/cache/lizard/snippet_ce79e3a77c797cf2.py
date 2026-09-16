def restore_ids(cls, obj, ids):
    ids = iter(ids)
    obj.traverse(lambda o: setattr(o, 'id', next(ids)))