def Group(params, name=None, type=None):
    atts = {}
    if name:
        atts['name'] = name
    if type:
        atts['type'] = type
    g = objectify.Element('Group', attrib=atts)
    for p in params:
        g.append(p)
    return g