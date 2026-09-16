def jinja_node_to_python(node):
    if isinstance(node, nodes.Const):
        return node.value
    if isinstance(node, nodes.Neg):
        return -jinja_node_to_python(node.node)
    if isinstance(node, nodes.Name):
        return node.name
    if isinstance(node, (nodes.List, nodes.Tuple)):
        value = []
        for i in node.items:
            value.append(jinja_node_to_python(i))
        return value
    if isinstance(node, nodes.Dict):
        value = {}
        for pair in node.items:
            value[pair.key.value] = jinja_node_to_python(pair.value)
        return value
    if isinstance(node, nodes.Call):
        if not isinstance(node.node, nodes.Name) or node.node.name not in ('_',
            'translate', 'gettext'):
            raise FormDefinitionError(
                'Cannot convert function calls from jinja to python other than translation calls'
                )
        return lazy_translate(jinja_node_to_python(node.args[0]))
    raise Exception('Cannot convert jinja nodes to python')