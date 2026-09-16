def get_sub_node(self, node):
    subnode = node.find('office:document')
    if subnode:
        mimetype = subnode.attrs['office:mimetype']
        self.type = MIMEMAP[mimetype]
        node = node.find('office:body')
    return node