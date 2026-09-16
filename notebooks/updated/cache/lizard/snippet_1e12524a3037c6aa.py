def convert_unicode(value):
    if isinstance(value, dict):
        return {convert_unicode(key): convert_unicode(value) for key, value in
            value.iteritems()}
    elif isinstance(value, list):
        return [convert_unicode(item) for item in value]
    elif isinstance(value, unicode):
        return value.encode('utf-8')
    else:
        return value