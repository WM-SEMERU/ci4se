def fromxml(node):
    if not isinstance(node, ElementTree._Element):
        node = parsexmlstring(node)
    assert node.tag.lower() == 'action'
    kwargs = {}
    args = []
    if 'id' in node.attrib:
        kwargs['id'] = node.attrib['id']
    elif 'name' in node.attrib:
        kwargs['name'] = node.attrib['name']
    elif 'description' in node.attrib:
        kwargs['description'] = node.attrib['description']
    elif 'method' in node.attrib:
        kwargs['method'] = node.attrib['method']
    elif 'mimetype' in node.attrib:
        kwargs['mimetype'] = node.attrib['mimetype']
    elif 'allowanonymous' in node.attrib:
        if node.attrib['allowanonymous'] == 'yes':
            kwargs['allowanonymous'] = True
    found = False
    for subnode in node:
        if subnode.tag.lower() == 'parametercondition':
            kwargs[node.tag] = ParameterCondition.fromxml(subnode)
        elif subnode.tag in vars(clam.common.parameters):
            args.append(vars(clam.common.parameters)[subnode.tag].fromxml(
                subnode))
    if not found:
        raise Exception('No condition found in ParameterCondition!')
    return Action(*args, **kwargs)