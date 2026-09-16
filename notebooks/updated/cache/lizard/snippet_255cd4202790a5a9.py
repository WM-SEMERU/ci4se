def var_spool_cwl_detector(obj, item=None, obj_key=None):
    r = False
    if isinstance(obj, string_types):
        if 'var/spool/cwl' in obj and obj_key != 'dockerOutputDirectory':
            _logger.warning(SourceLine(item=item, key=obj_key, raise_type=
                Text).makeError(_VAR_SPOOL_ERROR.format(obj)))
            r = True
    elif isinstance(obj, MutableMapping):
        for key, value in iteritems(obj):
            r = var_spool_cwl_detector(value, obj, key) or r
    elif isinstance(obj, MutableSequence):
        for key, value in enumerate(obj):
            r = var_spool_cwl_detector(value, obj, key) or r
    return r