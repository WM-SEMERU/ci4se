def cook_layout(layout, ajax):
    layout = re.sub('\r', '\n', re.sub('\r\n', '\n', layout))
    if isinstance(layout, six.text_type):
        result = getHTMLSerializer([layout.encode('utf-8')], encoding='utf-8')
    else:
        result = getHTMLSerializer([layout], encoding='utf-8')
    if '<![CDATA[' in layout:
        result.serializer = html.tostring
    all_slots = []
    for layoutPanelNode in slotsXPath(result.tree):
        data_slots = layoutPanelNode.attrib['data-slots']
        all_slots += wrap_append_prepend_slots(layoutPanelNode, data_slots)
        del layoutPanelNode.attrib['data-slots']
    if len(all_slots) == 0:
        for node in result.tree.xpath('//*[@data-panel="content"]'):
            wrap_append_prepend_slots(node,
                'content > body header main * content-core')
    head = result.tree.getroot().find('head')
    if not ajax and head is not None:
        for name in ['top_slot', 'head_slot', 'style_slot',
            'javascript_head_slot']:
            slot = etree.Element('{{{0:s}}}{1:s}'.format(NSMAP['metal'],
                name), nsmap=NSMAP)
            slot.attrib['define-slot'] = name
            head.append(slot)
    template = TEMPLATE
    metal = 'xmlns:metal="http://namespaces.zope.org/metal"'
    return (template % ''.join(result)).replace(metal, '')