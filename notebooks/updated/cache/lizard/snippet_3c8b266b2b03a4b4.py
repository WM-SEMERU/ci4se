def successors(self, node, exclude_compressed=True):
    succs = super(Graph, self).successors(node)
    if exclude_compressed:
        return [n for n in succs if not self.node[n].get('compressed', False)]
    else:
        return succs