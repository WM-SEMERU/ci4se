def id_to_root_name(id):
    name = root_names.get(id)
    if not name:
        name = repr(id)
    return name