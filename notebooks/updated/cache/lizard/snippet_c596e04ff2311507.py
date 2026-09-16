def get_field_definition(node):
    name = node.attrname
    cls = get_node_parent_class(node)
    definition = cls.lookup(name)[1][0].statement()
    return definition