def pydot__tree_to_png(tree, filename, rankdir='LR'):
    import pydot
    graph = pydot.Dot(graph_type='digraph', rankdir=rankdir)
    i = [0]

    def new_leaf(leaf):
        node = pydot.Node(i[0], label=repr(leaf))
        i[0] += 1
        graph.add_node(node)
        return node

    def _to_pydot(subtree):
        color = hash(subtree.data) & 16777215
        color |= 8421504
        subnodes = [(_to_pydot(child) if isinstance(child, Tree) else
            new_leaf(child)) for child in subtree.children]
        node = pydot.Node(i[0], style='filled', fillcolor='#%x' % color,
            label=subtree.data)
        i[0] += 1
        graph.add_node(node)
        for subnode in subnodes:
            graph.add_edge(pydot.Edge(node, subnode))
        return node
    _to_pydot(tree)
    graph.write_png(filename)