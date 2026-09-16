def makediagram(edges):
    graph = pydot.Dot(graph_type='digraph')
    nodes = edges2nodes(edges)
    epnodes = [(node, makeanode(node[0])) for node in nodes if nodetype(
        node) == 'epnode']
    endnodes = [(node, makeendnode(node[0])) for node in nodes if nodetype(
        node) == 'EndNode']
    epbr = [(node, makeabranch(node)) for node in nodes if not istuple(node)]
    nodedict = dict(epnodes + epbr + endnodes)
    for value in list(nodedict.values()):
        graph.add_node(value)
    for e1, e2 in edges:
        graph.add_edge(pydot.Edge(nodedict[e1], nodedict[e2]))
    return graph