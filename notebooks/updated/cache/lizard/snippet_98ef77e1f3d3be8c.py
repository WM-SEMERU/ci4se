def node(self, parent=None, tag='g', attrib=None, **extras):
    if parent is None:
        parent = self.root
    attrib = attrib or {}
    attrib.update(extras)

    def in_attrib_and_number(key):
        return key in attrib and isinstance(attrib[key], Number)
    for pos, dim in (('x', 'width'), ('y', 'height')):
        if in_attrib_and_number(dim) and attrib[dim] < 0:
            attrib[dim] = -attrib[dim]
            if in_attrib_and_number(pos):
                attrib[pos] = attrib[pos] - attrib[dim]
    for key, value in dict(attrib).items():
        if value is None:
            del attrib[key]
        attrib[key] = to_str(value)
        if key.endswith('_'):
            attrib[key.rstrip('_')] = attrib[key]
            del attrib[key]
        elif key == 'href':
            attrib[etree.QName('http://www.w3.org/1999/xlink', key)] = attrib[
                key]
            del attrib[key]
    return etree.SubElement(parent, tag, attrib)