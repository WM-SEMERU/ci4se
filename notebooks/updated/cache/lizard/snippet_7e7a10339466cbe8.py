def node2bracket(docgraph, node_id, child_str=''):
    node_attrs = docgraph.node[node_id]
    if istoken(docgraph, node_id):
        pos_str = node_attrs.get(docgraph.ns + ':pos', '')
        token_str = node_attrs[docgraph.ns + ':token']
        return '({pos}{space1}{token}{space2}{child})'.format(pos=pos_str,
            space1=bool(pos_str) * ' ', token=token_str, space2=bool(
            child_str) * ' ', child=child_str)
    label_str = node_attrs.get('label', '')
    return '({label}{space}{child})'.format(label=label_str, space=bool(
        label_str and child_str) * ' ', child=child_str)