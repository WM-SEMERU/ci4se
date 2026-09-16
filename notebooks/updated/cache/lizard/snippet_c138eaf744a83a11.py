def build_pydot(self, G=None):
    import pydot
    iamroot = False
    if G is None:
        G = pydot.Dot(graph_type='digraph', bgcolor=None)
        iamroot = True
    node = pydot.Node(id(self), shape='box', label=self.name)
    G.add_node(node)
    for child in self.parameters:
        child_node = child.build_pydot(G)
        G.add_edge(pydot.Edge(node, child_node))
    for _, o, _ in self.observers:
        label = o.name if hasattr(o, 'name') else str(o)
        observed_node = pydot.Node(id(o), label=label)
        if str(id(o)) not in G.obj_dict['nodes']:
            G.add_node(observed_node)
        edge = pydot.Edge(str(id(self)), str(id(o)), color='darkorange2',
            arrowhead='vee')
        G.add_edge(edge)
    if iamroot:
        return G
    return node