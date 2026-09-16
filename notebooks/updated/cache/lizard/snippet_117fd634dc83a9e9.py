def load(json_src, save=False):
    if isinstance(json_src, six.string_types):
        json_src = json_lib.loads(json_src)
    if isinstance(json_src, list):
        return [getattr(objects, obj['class']).load(obj, save) for obj in
            json_src]
    return getattr(objects, json_src['class']).load(json_src, save)