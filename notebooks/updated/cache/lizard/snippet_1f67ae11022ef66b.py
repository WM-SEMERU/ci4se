def add_node(self, node):
    if _debug:
        Network._debug('add_node %r', node)
    self.nodes.append(node)
    node.lan = self
    if not node.name:
        node.name = '%s:%s' % (self.name, node.address)