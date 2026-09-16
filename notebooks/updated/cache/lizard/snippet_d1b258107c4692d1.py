def construct(arg):
    if isinstance(arg, t.Trafaret):
        return arg
    elif isinstance(arg, tuple) or isinstance(arg, list) and len(arg) > 1:
        return t.Tuple(*(construct(a) for a in arg))
    elif isinstance(arg, list):
        return t.List(construct(arg[0]))
    elif isinstance(arg, dict):
        return t.Dict({construct_key(key): construct(value) for key, value in
            arg.items()})
    elif isinstance(arg, str):
        return t.Atom(arg)
    elif isinstance(arg, type):
        if arg is int:
            return t.Int()
        elif arg is float:
            return t.Float()
        elif arg is str:
            return t.String()
        elif arg is bool:
            return t.Bool()
        else:
            return t.Type(arg)
    elif callable(arg):
        return t.Call(arg)
    else:
        return arg