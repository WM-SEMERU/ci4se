def get_transformer(name, base=None, *args, **kwargs):
    name = name.lower()
    if base is None:
        base = ['extractors', 'converters', 'filters']
    base = listify(base)
    for b in base:
        importlib.import_module('pliers.%s' % b)
        mod = getattr(pliers, b)
        classes = getattr(mod, '__all__')
        for cls_name in classes:
            if cls_name.lower() == name.lower():
                cls = getattr(mod, cls_name)
                return cls(*args, **kwargs)
    raise KeyError("No transformer named '%s' found." % name)