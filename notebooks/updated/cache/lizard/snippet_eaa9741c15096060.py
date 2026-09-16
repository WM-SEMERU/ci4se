def prompt_config(sch, defaults=None, path=None):
    out = {}
    for name, attr in sch.attributes():
        fullpath = name
        if path:
            fullpath = '{}.{}'.format(path, name)
        if defaults is None:
            defaults = {}
        default = defaults.get(name)
        if isinstance(attr, _schema.Schema):
            value = prompt_config(attr, defaults=default, path=fullpath)
        else:
            if default is None:
                default = attr.default
            if default is None:
                default = ''
            value = prompt(fullpath, default)
        out[name] = value
    return sch.validate(out)