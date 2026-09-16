def _any(confs=None, **kwargs):
    result = False
    if confs is not None:
        if isinstance(confs, string_types) or isinstance(confs, dict):
            confs = [confs]
        for conf in confs:
            result = run(conf, **kwargs)
            if result:
                break
    return result