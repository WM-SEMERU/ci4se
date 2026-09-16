def extends_(cls, kls):
    if inspect.isclass(kls):
        for _name, _val in kls.__dict__.items():
            if not _name.startswith('__'):
                setattr(cls, _name, _val)
    elif inspect.isfunction(kls):
        setattr(cls, kls.__name__, kls)
    return cls