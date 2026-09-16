def rename_collection(db, collection, new_name):
    if hasattr(new_name, '__call__'):
        _new = new_name(collection)
        if _new == '':
            return
    else:
        _new = new_name
    c = db[collection]
    c.rename(_new)