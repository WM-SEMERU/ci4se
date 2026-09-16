def encode_relation(relation: BioCRelation):
    tree = etree.Element('relation', {'id': relation.id})
    encode_infons(tree, relation.infons)
    for node in relation.nodes:
        tree.append(encode_node(node))
    return tree