def merge_rootnodes(self, other_docgraph):
    if 'metadata' in other_docgraph.node[other_docgraph.root]:
        other_meta = other_docgraph.node[other_docgraph.root]['metadata']
        self.node[self.root]['metadata'].update(other_meta)
    assert not other_docgraph.in_edges(other_docgraph.root
        ), "root node in graph '{}' must not have any ingoing edges".format(
        other_docgraph.name)
    for root, target, attrs in other_docgraph.out_edges(other_docgraph.root,
        data=True):
        self.add_edge(self.root, target, attr_dict=attrs)
    self.remove_node(other_docgraph.root)