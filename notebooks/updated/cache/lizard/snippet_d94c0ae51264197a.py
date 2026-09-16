def get_aspect(cx, aspect_name):
    if isinstance(cx, dict):
        return cx.get(aspect_name)
    for entry in cx:
        if list(entry.keys())[0] == aspect_name:
            return entry[aspect_name]