def bencode(obj):
    if isinstance(obj, int):
        return 'i' + str(obj) + 'e'
    if isinstance(obj, str):
        if not obj:
            return None
        return str(len(obj)) + ':' + obj
    if isinstance(obj, list):
        res = 'l'
        for elem in obj:
            elem = bencode(elem)
            if elem:
                res += elem
        return res + 'e'
    if isinstance(obj, dict):
        res = 'd'
        for key in sorted(obj.keys()):
            if key in obj:
                value = bencode(obj[key])
                key = bencode(key)
                if key and value:
                    res += key + value
        return res + 'e'
    if isinstance(obj, unicode):
        return bencode(obj.encode('utf-8'))
    if isinstance(obj, collections.OrderedDict):
        return bencode(dict(obj))
    raise Exception('Unknown object: %s (%s)' % (repr(obj), repr(type(obj))))