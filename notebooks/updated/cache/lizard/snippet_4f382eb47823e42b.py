def get_unique_name(name='', collection=()):
    if name not in collection:
        return name
    i = 1
    while True:
        i += 1
        name2 = '%s_%s' % (name, i)
        if name2 not in collection:
            return name2