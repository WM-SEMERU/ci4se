def convert_node(self, node):
    convert = getattr(self, 'convert_' + striptag(node.tag))
    return convert(node)