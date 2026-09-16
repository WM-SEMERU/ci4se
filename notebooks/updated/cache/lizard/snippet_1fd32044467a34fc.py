def _compact_class_repr(obj):
    dict_str_list = []
    post_repr_string = ''
    init_func = obj.__init__
    if _sys.version_info.major == 2:
        init_func = init_func.__func__
    fields = _inspect.getargspec(init_func).args
    fields = fields[1:]
    if 'features' in fields:
        fields.remove('features')
        features = obj.get('features')
        if features is not None:
            post_repr_string = ' on %s feature(s)' % len(features)
    if 'excluded_features' in fields:
        fields.remove('excluded_features')
    if issubclass(obj.__class__, _Transformer):
        for attr in fields:
            dict_str_list.append('%s=%s' % (attr, obj.get(attr).__repr__()))
    elif obj.__class__ == TransformerChain:
        _step_classes = list(map(lambda x: x.__class__.__name__, obj.get(
            'steps')))
        _steps = _internal_utils.pretty_print_list(_step_classes, 'steps',
            False)
        dict_str_list.append(_steps)
    else:
        for attr in fields:
            dict_str_list.append('%s=%s' % (attr, obj.__dict__[attr]))
    return '%s(%s)%s' % (obj.__class__.__name__, ', '.join(dict_str_list),
        post_repr_string)