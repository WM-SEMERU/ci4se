def snake_case_methods(cls, debug=False):
    if not CONVERT_SNAKE_CASE:
        return cls
    root_base = cls._ROOT
    members = inspect.getmembers(root_base)
    names = {}
    for name, member in members:
        lower_name = name.lower()
        if lower_name in names:
            del names[lower_name]
        else:
            names[lower_name] = None
    for name, member in members:
        if name.lower() not in names:
            continue
        if name[0] == '_' or name.islower():
            continue
        if not inspect.ismethod(member) and not inspect.isfunction(member):
            continue
        new_name = camel_to_snake(name)
        value = None
        skip = False
        for c in cls.mro():
            if new_name in c.__dict__:
                skip = True
                break
            if name in c.__dict__:
                value = c.__dict__[name]
                break
        else:
            value = getattr(cls, name)
        if skip:
            continue
        setattr(cls, new_name, value)
    return cls