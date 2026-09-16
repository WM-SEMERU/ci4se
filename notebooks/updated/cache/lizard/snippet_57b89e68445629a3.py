def _fix_tagging(value, params):
    _tag_type_to_explicit_implicit(params)
    retag = False
    if 'implicit' not in params:
        if value.implicit is not False:
            retag = True
    else:
        if isinstance(params['implicit'], tuple):
            class_, tag = params['implicit']
        else:
            tag = params['implicit']
            class_ = 'context'
        if value.implicit is False:
            retag = True
        elif value.class_ != CLASS_NAME_TO_NUM_MAP[class_] or value.tag != tag:
            retag = True
    if params.get('explicit') != value.explicit:
        retag = True
    if retag:
        return value.retag(params)
    return value