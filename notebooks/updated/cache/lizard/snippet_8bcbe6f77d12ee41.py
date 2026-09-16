def casefold(s, fullcasefold=True, useturkicmapping=False):
    if not isinstance(s, six.text_type):
        raise TypeError("String to casefold must be of type 'unicode'!")
    lookup_order = 'CF'
    if not fullcasefold:
        lookup_order = 'CS'
    if useturkicmapping:
        lookup_order = 'T' + lookup_order
    return ''.join([casefold_map.lookup(c, lookup_order=lookup_order) for c in
        preservesurrogates(s)])