def get_importer(cls, name):
    if name not in importer_index:
        raise TypeError("importer type '%s' is not registered: " % name + 
            'registered types: %r' % sorted(importer_index.keys()))
    for base_class in importer_index[name]:
        if issubclass(cls, base_class):
            return importer_index[name][base_class](cls)
    raise TypeError("importer type '%s' for a %r is not registered" % (name,
        cls))