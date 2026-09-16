def _list_class_vars(cls, exclude=None):
    cvars = {k: v for k, v in vars(cls).items() if not k.startswith('_')}
    cvars = deepcopy(cvars)
    if exclude is not None:
        for e in exclude:
            cvars.pop(e)
    return cvars