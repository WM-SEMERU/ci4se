def make_mapping(args):
    mapping = {}
    if args:
        for arg in args:
            name_value = arg.split('=', 1)
            mapping[name_value[0]] = name_value[1] if len(name_value
                ) > 1 else None
    return mapping