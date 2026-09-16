def add_nodes(self, nodes, nesting=1):
    hopNodes = set()
    hopEdges = []
    for i, n in zip(range(len(nodes)), nodes):
        r, g, b = rainbowcolour(i, len(nodes))
        colour = '#%02X%02X%02X' % (r, g, b)
        for ne in n.efferent:
            if ne not in self.added:
                hopNodes.add(ne)
            hopEdges.append((ne, n, 'solid', colour))
    self.add_to_graph(hopNodes, hopEdges, nesting)