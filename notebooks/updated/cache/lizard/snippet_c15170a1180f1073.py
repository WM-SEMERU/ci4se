def build_expected(dynamizer, expected):
    ret = {}
    for k, v in six.iteritems(expected):
        if is_null(v):
            ret[k] = {'Exists': False}
        else:
            ret[k] = {'Exists': True, 'Value': dynamizer.encode(v)}
    return ret