def to_networkx(self):
    try:
        from networkx import DiGraph, set_node_attributes
    except ImportError:
        raise ImportError(
            'You must have networkx installed to export networkx graphs')
    result = DiGraph()
    for row in self._raw_tree:
        result.add_edge(row['parent'], row['child'], weight=row['lambda_val'])
    set_node_attributes(result, dict(self._raw_tree[['child', 'child_size']
        ]), 'size')
    return result