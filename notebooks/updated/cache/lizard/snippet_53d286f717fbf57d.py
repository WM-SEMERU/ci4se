def toTypeURIs(namespace_map, alias_list_s):
    uris = []
    if alias_list_s:
        for alias in alias_list_s.split(','):
            type_uri = namespace_map.getNamespaceURI(alias)
            if type_uri is None:
                raise KeyError('No type is defined for attribute name %r' %
                    (alias,))
            else:
                uris.append(type_uri)
    return uris