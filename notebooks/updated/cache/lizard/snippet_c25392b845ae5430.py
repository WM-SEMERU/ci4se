def grok_for_node(element, default_vars):
    if isinstance(element.iter, jinja2.nodes.Filter):
        if (element.iter.name == 'default' and element.iter.node.name not in
            default_vars):
            default_vars.append(element.iter.node.name)
        default_vars = default_vars + grok_vars(element)
    return default_vars