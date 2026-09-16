def _get_graphics(dom):
    out = {'autoport': 'None', 'keymap': 'None', 'listen': 'None', 'port':
        'None', 'type': 'None'}
    doc = ElementTree.fromstring(dom.XMLDesc(0))
    for g_node in doc.findall('devices/graphics'):
        for key, value in six.iteritems(g_node.attrib):
            out[key] = value
    return out