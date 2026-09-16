def loads(s: str, load_module: types.ModuleType, **kwargs):
    return json.loads(s, object_hook=lambda pairs: loads_loader(load_module,
        pairs), **kwargs)