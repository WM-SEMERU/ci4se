def load_uri(uri, base_uri=None, loader=None, jsonschema=False,
    load_on_repr=True):
    if loader is None:
        loader = jsonloader
    if base_uri is None:
        base_uri = uri
    return JsonRef.replace_refs(loader(uri), base_uri=base_uri, loader=
        loader, jsonschema=jsonschema, load_on_repr=load_on_repr)