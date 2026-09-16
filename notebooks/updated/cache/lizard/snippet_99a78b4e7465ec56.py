def set_formatter(name, func):
    if name in ('self', 'instance', 'this'):
        global af_self
        af_self = _formatter_self if func is None else func
    elif name == 'class':
        global af_class
        af_class = _formatter_class if func is None else func
    elif name in ('named', 'param', 'parameter'):
        global af_named
        af_named = _formatter_named if func is None else func
    elif name in ('default', 'optional'):
        global af_default
        af_default = _formatter_defaults if func is None else func
    elif name in ('anonymous', 'arbitrary', 'unnamed'):
        global af_anonymous
        af_anonymous = chop if func is None else func
    elif name in ('keyword', 'pair', 'pairs'):
        global af_keyword
        af_keyword = _formatter_named if func is None else func
    else:
        raise ValueError('unknown trace formatter %r' % name)