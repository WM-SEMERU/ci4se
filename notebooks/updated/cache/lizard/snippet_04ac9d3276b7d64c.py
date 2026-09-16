def multidict_to_dict(d):
    return dict((k, v[0] if len(v) == 1 else v) for k, v in iterlists(d))