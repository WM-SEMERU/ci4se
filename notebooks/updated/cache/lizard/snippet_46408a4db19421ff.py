def mavlink_to_json(msg):
    ret = '"%s": {' % msg._type
    for fieldname in msg._fieldnames:
        data = getattr(msg, fieldname)
        ret += '"%s" : "%s", ' % (fieldname, data)
    ret = ret[0:-2] + '}'
    return ret