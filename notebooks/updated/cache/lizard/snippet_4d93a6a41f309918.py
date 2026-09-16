def new_geom(geom_type, size, pos=(0, 0, 0), rgba=RED, group=0, **kwargs):
    kwargs['type'] = str(geom_type)
    kwargs['size'] = array_to_string(size)
    kwargs['rgba'] = array_to_string(rgba)
    kwargs['group'] = str(group)
    kwargs['pos'] = array_to_string(pos)
    element = ET.Element('geom', attrib=kwargs)
    return element