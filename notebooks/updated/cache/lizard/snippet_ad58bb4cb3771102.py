def extract_arguments(args, prefix=DATA_PREFIX):
    data = {}
    for key, value in iteritems(args.__dict__):
        if key.startswith(prefix) and value is not None:
            parts = key[len(prefix):].split('__')
            d = data
            for p in parts[:-1]:
                assert p not in d or isinstance(d[p], dict)
                d = d.setdefault(p, {})
            d[parts[-1]] = value if value != '' else None
    return data