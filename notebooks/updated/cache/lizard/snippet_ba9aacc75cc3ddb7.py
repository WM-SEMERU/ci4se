def transform_flask_from_long(node):
    actual_module_name = make_non_magical_flask_import(node.modname)
    new_node = nodes.ImportFrom(actual_module_name, node.names, node.level)
    copy_node_info(node, new_node)
    mark_transformed(new_node)
    return new_node