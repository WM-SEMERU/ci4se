def repack_dictlist(data, strict=False, recurse=False, key_cb=None, val_cb=None
    ):
    if isinstance(data, six.string_types):
        try:
            data = salt.utils.yaml.safe_load(data)
        except salt.utils.yaml.parser.ParserError as err:
            log.error(err)
            return {}
    if key_cb is None:
        key_cb = lambda x: x
    if val_cb is None:
        val_cb = lambda x, y: y
    valid_non_dict = six.string_types, six.integer_types, float
    if isinstance(data, list):
        for element in data:
            if isinstance(element, valid_non_dict):
                continue
            elif isinstance(element, dict):
                if len(element) != 1:
                    log.error(
                        'Invalid input for repack_dictlist: key/value pairs must contain only one element (data passed: %s).'
                        , element)
                    return {}
            else:
                log.error(
                    'Invalid input for repack_dictlist: element %s is not a string/dict/numeric value'
                    , element)
                return {}
    else:
        log.error(
            'Invalid input for repack_dictlist, data passed is not a list (%s)'
            , data)
        return {}
    ret = {}
    for element in data:
        if isinstance(element, valid_non_dict):
            ret[key_cb(element)] = None
        else:
            key = next(iter(element))
            val = element[key]
            if is_dictlist(val):
                if recurse:
                    ret[key_cb(key)] = repack_dictlist(val, recurse=recurse)
                elif strict:
                    log.error(
                        'Invalid input for repack_dictlist: nested dictlist found, but recurse is set to False'
                        )
                    return {}
                else:
                    ret[key_cb(key)] = val_cb(key, val)
            else:
                ret[key_cb(key)] = val_cb(key, val)
    return ret