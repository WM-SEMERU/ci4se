def make_class_dictable(cls, exclude=constants.default_exclude,
    exclude_underscore=constants.default_exclude_underscore,
    fromdict_allow_pk=constants.default_fromdict_allow_pk, include=None,
    asdict_include=None, fromdict_include=None):
    setattr(cls, 'dictalchemy_exclude', exclude)
    setattr(cls, 'dictalchemy_exclude_underscore', exclude_underscore)
    setattr(cls, 'dictalchemy_fromdict_allow_pk', fromdict_allow_pk)
    setattr(cls, 'asdict', asdict)
    setattr(cls, 'fromdict', fromdict)
    setattr(cls, '__iter__', iter)
    setattr(cls, 'dictalchemy_include', include)
    setattr(cls, 'dictalchemy_asdict_include', asdict_include)
    setattr(cls, 'dictalchemy_fromdict_include', fromdict_include)
    return cls