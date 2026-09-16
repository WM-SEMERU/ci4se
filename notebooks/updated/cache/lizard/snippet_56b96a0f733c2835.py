def transform_flask_bare_import(node):
    new_names = []
    for name, as_name in node.names:
        match = re.match('flask\\.ext\\.(.*)', name)
        from_name = match.group(1)
        actual_module_name = 'flask_{}'.format(from_name)
        new_names.append((actual_module_name, as_name))
    new_node = nodes.Import()
    copy_node_info(node, new_node)
    new_node.names = new_names
    mark_transformed(new_node)
    return new_node