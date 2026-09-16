def add_group(self, group_attribs=None, parent=None):
    if parent is None:
        parent = self.tree.getroot()
    elif not self.contains_group(parent):
        warnings.warn(
            'The requested group {0} does not belong to this Document'.
            format(parent))
    if group_attribs is None:
        group_attribs = {}
    else:
        group_attribs = group_attribs.copy()
    return SubElement(parent, '{{{0}}}g'.format(SVG_NAMESPACE['svg']),
        group_attribs)