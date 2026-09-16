def replace(self, nodes, node):
    nodes = nodes if isinstance(nodes, list) else [nodes]
    collapse = self.id(node) in self.nodes
    if not collapse:
        self.add_node(node)
    for in_node in self.incoming(nodes):
        self.add_edge(in_node, node, in_node.output_shape if hasattr(
            in_node, 'output_shape') else None)
    for out_node in self.outgoing(nodes):
        self.add_edge(node, out_node, node.output_shape if hasattr(node,
            'output_shape') else None)
    for n in nodes:
        if collapse and n == node:
            continue
        self.remove(n)