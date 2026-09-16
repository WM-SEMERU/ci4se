def add_node(self, node):
    other_nodes = [n for n in self.nodes() if n.id != node.id]
    for n in other_nodes:
        if isinstance(n, Source):
            node.connect(direction='from', whom=n)
        else:
            node.connect(direction='both', whom=n)