def construct_mapping(self, node, deep=False):
    mapping = ODict()
    for key_node, value_node in node.value:
        key = self.construct_object(key_node, deep=deep)
        value = self.construct_object(value_node, deep=deep)
        mapping[key] = value
    return mapping