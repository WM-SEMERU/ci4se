def camel_to_underscore(name):
    as_list = []
    length = len(name)
    for index, i in enumerate(name):
        if index != 0 and index != length - 1 and i.isupper():
            as_list.append('_%s' % i.lower())
        else:
            as_list.append(i.lower())
    return ''.join(as_list)