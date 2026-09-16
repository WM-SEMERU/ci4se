def decode_dict(data, encoding=None, errors='strict', keep=False, normalize
    =False, preserve_dict_class=False, preserve_tuples=False, to_str=False):
    _decode_func = (salt.utils.stringutils.to_unicode if not to_str else
        salt.utils.stringutils.to_str)
    rv = data.__class__() if preserve_dict_class else {}
    for key, value in six.iteritems(data):
        if isinstance(key, tuple):
            key = decode_tuple(key, encoding, errors, keep, normalize,
                preserve_dict_class, to_str
                ) if preserve_tuples else decode_list(key, encoding, errors,
                keep, normalize, preserve_dict_class, preserve_tuples, to_str)
        else:
            try:
                key = _decode_func(key, encoding, errors, normalize)
            except TypeError:
                pass
            except UnicodeDecodeError:
                if not keep:
                    raise
        if isinstance(value, list):
            value = decode_list(value, encoding, errors, keep, normalize,
                preserve_dict_class, preserve_tuples, to_str)
        elif isinstance(value, tuple):
            value = decode_tuple(value, encoding, errors, keep, normalize,
                preserve_dict_class, to_str
                ) if preserve_tuples else decode_list(value, encoding,
                errors, keep, normalize, preserve_dict_class,
                preserve_tuples, to_str)
        elif isinstance(value, Mapping):
            value = decode_dict(value, encoding, errors, keep, normalize,
                preserve_dict_class, preserve_tuples, to_str)
        else:
            try:
                value = _decode_func(value, encoding, errors, normalize)
            except TypeError:
                pass
            except UnicodeDecodeError:
                if not keep:
                    raise
        rv[key] = value
    return rv