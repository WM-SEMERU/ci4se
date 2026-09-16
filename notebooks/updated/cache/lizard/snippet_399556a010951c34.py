def flatten(value, prefix=None):

    def issimple(value):
        for item in value:
            if isinstance(item, dict) or isinstance(item, list):
                return False
        return True
    if isinstance(value, six.text_type):
        return value.encode('utf8')
    if isinstance(value, list):
        if issimple(value):
            return value
        offset = 0
        result = {}
        prefix = '%d' if prefix is None else '%s_%%d' % prefix
        for item in value:
            k = prefix % offset
            v = flatten(item, k)
            if not isinstance(v, dict):
                v = {k: v}
            result.update(v)
            offset += 1
        return result
    if isinstance(value, dict):
        result = {}
        prefix = '%s' if prefix is None else '%s_%%s' % prefix
        for k, v in six.iteritems(value):
            k = prefix % str(k)
            v = flatten(v, k)
            if not isinstance(v, dict):
                v = {k: v}
            result.update(v)
        return result
    return value