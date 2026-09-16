def _convert(cls, name, module, filter, source=None):
    module_globals = vars(_sys.modules[module])
    if source:
        source = vars(source)
    else:
        source = module_globals
    members = dict((name, value) for name, value in source.items() if
        filter(name))
    cls = cls(name, members, module=module)
    cls.__reduce_ex__ = _reduce_ex_by_name
    module_globals.update(cls.__members__)
    module_globals[name] = cls
    return cls