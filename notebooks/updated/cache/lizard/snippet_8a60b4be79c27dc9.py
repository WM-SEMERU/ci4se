def convert_to_geoff(discoursegraph):
    dg_copy = deepcopy(discoursegraph)
    layerset2list(dg_copy)
    add_node_ids_as_labels(dg_copy)
    return graph2geoff(dg_copy, 'LINKS_TO')